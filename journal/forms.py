from django import forms
from journal.models import JournalEntry, MoodTag


class JournalEntryForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=MoodTag.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = JournalEntry

        fields = (
            "title",
            "content",
            "mood_score",
            "tags",
        )
