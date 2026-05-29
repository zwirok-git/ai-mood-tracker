from django.contrib.auth import get_user_model
from django.test import TestCase

from journal.models import (
    JournalEntry,
    MoodTag,
)

User = get_user_model()


class JournalModelsTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="alex",
            password="password123",
        )

    def test_create_entry(self):
        entry = JournalEntry.objects.create(
            user=self.user,
            title="Test",
            content="Content",
            mood_score=7,
        )

        self.assertEqual(
            entry.title,
            "Test",
        )

    def test_mood_tag_string(self):
        tag = MoodTag.objects.create(
            name="Happy",
            emoji="😊",
            color="#FFFF00",
        )

        self.assertEqual(
            str(tag),
            "😊 Happy",
        )

    def test_journal_ordering(self):
        self.assertEqual(
            JournalEntry._meta.ordering,
            ["-created_at"],
        )
