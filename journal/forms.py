from django import forms
from django.contrib.auth.forms import AuthenticationForm
from journal.models import JournalEntry


class UserLoginForm (AuthenticationForm):
    pass


class JournalEntryForm(forms.ModelForm):

    class Meta:
        model = JournalEntry

        fields = (
            "title",
            "content",
            "mood_score",
        )
