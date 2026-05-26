from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from journal.models import JournalEntry, MoodTag


class UserLoginForm(AuthenticationForm):
    pass


class UserSignupForm(SignupForm):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)

    def save(self, request):
        user = super().save(request)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.save(update_fields=["first_name", "last_name"])

        return user


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
