from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from journal.models import JournalEntry


class JournalEntryListView(LoginRequiredMixin, generic.ListView):
    model = JournalEntry
    template_name = "journal/journal_entry/journal_entry_list.html"
    paginate_by = 10

    def get_queryset(self):
        return JournalEntry.objects.filter(user=self.request.user)


class JournalEntryCreateView:
    pass


class JournalEntryUpdateView:
    pass


class JournalEntryDeleteView:
    pass


class JournalEntryDetailView:
    pass