from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.views import generic

from journal.forms import JournalEntryForm
from journal.models import JournalEntry


class JournalEntryListView(LoginRequiredMixin, generic.ListView):
    model = JournalEntry
    template_name = "journal/journal_entry/journal_entry_list.html"
    paginate_by = 10

    def get_queryset(self):
        return JournalEntry.objects.filter(user=self.request.user)


class JournalEntryCreateView(LoginRequiredMixin, generic.CreateView):
    model = JournalEntry
    form_class = JournalEntryForm
    template_name = "journal/journal_entry/journal_entry_form.html"
    success_url = reverse_lazy("journal:journal-entry-list")

    def form_valid(self, form,):
        form.instance.user = self.request.user

        return super().form_valid(form)




class JournalEntryUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = JournalEntry
    template_name = "journal/journal_entry/journal_entry_form.html"
    form_class = JournalEntryForm

    def get_success_url(self):
        return reverse("journal:entry", args=[self.object.pk],
        )

    def test_func(self):
        return self.get_object().user == self.request.user


class JournalEntryDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = JournalEntry
    template_name = "journal/journal_entry/journal_entry_delete.html"
    success_url = reverse_lazy("journal:journal-entry-list")

    def test_func(self):
        return self.get_object().user == self.request.user


class JournalEntryDetailView(LoginRequiredMixin, UserPassesTestMixin, generic.DetailView):
    model = JournalEntry
    template_name = "journal/journal_entry/journal_entry_detail.html"

    def test_func(self):
        return self.get_object().user == self.request.user
