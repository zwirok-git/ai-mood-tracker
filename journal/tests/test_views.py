from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from journal.models import JournalEntry


User = get_user_model()


class JournalViewsTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="alex",
            password="password123",
        )

        self.other = User.objects.create_user(
            username="other",
            password="password123",
        )

        self.entry = JournalEntry.objects.create(
            user=self.user,
            title="Test",
            content="Entry",
            mood_score=7,
        )

    def login(self):
        self.client.login(
            username="alex",
            password="password123",
        )

    def test_list_requires_login(self):
        response = self.client.get(
            reverse(
                "journal:journal-entry-list"
            )
        )

        self.assertEqual(
            response.status_code,
            302,
        )

    def test_list_page(self):
        self.login()

        response = self.client.get(
            reverse(
                "journal:journal-entry-list"
            )
        )

        self.assertEqual(
            response.status_code,
            200,
        )

    def test_create_entry(self):
        self.login()

        response = self.client.post(
            reverse(
                "journal:entry-create"
            ),
            {
                "title": "Created",
                "content": "Text",
                "mood_score": 5,
            },
        )

        self.assertEqual(
            response.status_code,
            302,
        )

        self.assertTrue(
            JournalEntry.objects.filter(
                title="Created"
            ).exists()
        )

    def test_detail_owner_only(self):
        self.login()

        response = self.client.get(
            reverse(
                "journal:entry",
                args=[self.entry.pk],
            )
        )

        self.assertEqual(
            response.status_code,
            200,
        )

    def test_other_user_cannot_open(self):
        self.client.login(
            username="other",
            password="password123",
        )

        response = self.client.get(
            reverse(
                "journal:entry",
                args=[self.entry.pk],
            )
        )

        self.assertEqual(
            response.status_code,
            403,
        )

    def test_delete_entry(self):
        self.login()

        response = self.client.post(
            reverse(
                "journal:entry-delete",
                args=[self.entry.pk],
            )
        )

        self.assertEqual(
            response.status_code,
            302,
        )

        self.assertFalse(
            JournalEntry.objects.filter(
                pk=self.entry.pk
            ).exists()
        )