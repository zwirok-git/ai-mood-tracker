import re
from urllib.parse import urlparse

from allauth.account.models import EmailAddress
from django.contrib.auth import get_user_model
from django.core import mail
from django.test import TestCase, override_settings
from django.urls import reverse

from journal.models import JournalEntry


class JournalEntryPermissionsTests(TestCase):
    def setUp(self):
        self.owner = get_user_model().objects.create_user(
            username="owner",
            password="strong-test-password",
        )
        self.other_user = get_user_model().objects.create_user(
            username="other",
            password="strong-test-password",
        )
        self.entry = JournalEntry.objects.create(
            user=self.owner,
            title="Private entry",
            content="This should stay private.",
            mood_score=5,
        )

    def test_other_user_cannot_view_entry(self):
        self.client.force_login(self.other_user)

        response = self.client.get(reverse("journal:entry", args=[self.entry.pk]))

        self.assertEqual(response.status_code, 403)

    def test_other_user_cannot_update_entry(self):
        self.client.force_login(self.other_user)

        response = self.client.post(
            reverse("journal:entry-edit", args=[self.entry.pk]),
            {
                "title": "Changed by other user",
                "content": "Changed content",
                "mood_score": 1,
            },
        )

        self.assertEqual(response.status_code, 403)
        self.entry.refresh_from_db()
        self.assertEqual(self.entry.title, "Private entry")
        self.assertEqual(self.entry.content, "This should stay private.")

    def test_other_user_cannot_delete_entry(self):
        self.client.force_login(self.other_user)

        response = self.client.post(reverse("journal:entry-delete", args=[self.entry.pk]))

        self.assertEqual(response.status_code, 403)
        self.assertTrue(JournalEntry.objects.filter(pk=self.entry.pk).exists())


@override_settings(
    ALLOWED_HOSTS=["testserver"],
    EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend",
)
class RegistrationTests(TestCase):
    def test_signup_sends_verification_email(self):
        response = self.client.post(
            reverse("register"),
            {
                "username": "newuser",
                "email": "newuser-signup@example.com",
                "first_name": "New",
                "last_name": "User",
                "password1": "strong-test-password",
                "password2": "strong-test-password",
            },
        )

        self.assertEqual(response.status_code, 302)
        user = get_user_model().objects.get(username="newuser")
        email_address = EmailAddress.objects.get(user=user, email="newuser-signup@example.com")

        self.assertTrue(user.is_active)
        self.assertFalse(email_address.verified)
        self.assertEqual(len(mail.outbox), 1)

    def test_email_confirmation_activates_user(self):
        self.client.post(
            reverse("register"),
            {
                "username": "confirmeduser",
                "email": "confirmeduser@example.com",
                "first_name": "New",
                "last_name": "User",
                "password1": "strong-test-password",
                "password2": "strong-test-password",
            },
        )
        confirmation_url = re.search(
            r"http://testserver(?P<path>/accounts/confirm-email/[^\s]+/)",
            mail.outbox[0].body,
        )
        self.assertIsNotNone(confirmation_url)

        self.client.get(urlparse(confirmation_url.group("path")).path)

        user = get_user_model().objects.get(username="confirmeduser")
        email_address = EmailAddress.objects.get(user=user, email="confirmeduser@example.com")
        self.assertTrue(email_address.verified)
