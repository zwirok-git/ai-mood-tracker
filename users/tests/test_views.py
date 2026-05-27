from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


User = get_user_model()


class UserViewsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="alex",
            password="password123",
            email="alex@test.com",
        )

    def login(self):
        self.client.login(
            username="alex",
            password="password123",
        )

    def test_profile_requires_login(self):
        response = self.client.get(
            reverse(
                "account:profile",
                args=[self.user.id],
            )
        )

        self.assertEqual(
            response.status_code,
            302,
        )

    def test_profile_page(self):
        self.login()

        response = self.client.get(
            reverse(
                "account:profile",
                args=[self.user.id],
            )
        )

        self.assertEqual(
            response.status_code,
            200,
        )

    def test_update_profile(self):
        self.login()

        response = self.client.post(
            reverse(
                "account:profile-edit",
                args=[self.user.id],
            ),
            {
                "username": "newname",
                "email": "new@test.com",
                "first_name": "Alex",
                "last_name": "Updated",
            },
        )

        self.user.refresh_from_db()

        self.assertEqual(
            response.status_code,
            302,
        )

        self.assertEqual(
            self.user.username,
            "newname",
        )