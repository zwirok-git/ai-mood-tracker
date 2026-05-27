from django.test import TestCase

from journal.forms import JournalEntryForm
from journal.models import MoodTag


class JournalEntryFormTests(TestCase):

    def test_form_valid(self):
        tag = MoodTag.objects.create(
            name="Happy",
            emoji="😊",
            color="#ffffff",
        )

        form = JournalEntryForm(
            data={
                "title": "Entry",
                "content": "Today good",
                "mood_score": 8,
                "tags": [tag.id],
            }
        )

        self.assertTrue(
            form.is_valid()
        )

    def test_invalid_mood_score(self):
        form = JournalEntryForm(
            data={
                "title": "Entry",
                "content": "Text",
                "mood_score": 20,
            }
        )

        self.assertFalse(
            form.is_valid()
        )