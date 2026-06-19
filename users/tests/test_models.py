from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()


class UserModelTests(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(
            username="alex",
            password="password123",
        )

        self.assertEqual(
            user.username,
            "alex",
        )

    def test_string_representation(self):
        user = User.objects.create_user(
            username="alex",
        )

        self.assertEqual(
            str(user),
            "alex",
        )
