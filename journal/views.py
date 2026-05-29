from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.views import generic, View

from journal.forms import JournalEntryForm
from journal.mixins import JournalOwnerRequiredMixin
from journal.models import JournalEntry
from journal.services.insight_service.insight_service import InsightService


class JournalEntryListView(LoginRequiredMixin, generic.ListView):
    model = JournalEntry
    template_name = "journal/journal_entry/journal_entry_list.html"
    paginate_by = 2

    def get_queryset(self):
        return JournalEntry.objects.filter(user=self.request.user).prefetch_related(
            "tags"
        )


class JournalEntryCreateView(LoginRequiredMixin, generic.CreateView):
    model = JournalEntry
    form_class = JournalEntryForm
    template_name = "journal/journal_entry/journal_entry_form.html"
    success_url = reverse_lazy("journal:journal-entry-list")

    def form_valid(
        self,
        form,
    ):
        form.instance.user = self.request.user

        return super().form_valid(form)


class JournalEntryUpdateView(
    LoginRequiredMixin, JournalOwnerRequiredMixin, generic.UpdateView
):
    model = JournalEntry
    template_name = "journal/journal_entry/journal_entry_form.html"
    form_class = JournalEntryForm

    def get_success_url(self):
        return reverse("journal:entry", args=[self.object.pk])


class JournalEntryDeleteView(
    LoginRequiredMixin, JournalOwnerRequiredMixin, generic.DeleteView
):
    model = JournalEntry
    template_name = "journal/journal_entry/journal_entry_delete.html"
    success_url = reverse_lazy("journal:journal-entry-list")


class JournalEntryDetailView(
    LoginRequiredMixin, JournalOwnerRequiredMixin, generic.DetailView
):
    model = JournalEntry
    template_name = "journal/journal_entry/journal_entry_detail.html"


class IndexView(generic.TemplateView):
    template_name = "landing.html"


class GenerateInsightView(LoginRequiredMixin, View):
    def post(self, request, pk):
        entry = get_object_or_404(
            JournalEntry,
            pk=pk,
            user=request.user,
        )

        regenerate = request.POST.get("regenerate") == "true"

        insight = InsightService().generate_insight(entry=entry, regenerate=regenerate)

        entry.refresh_from_db()

        return render(
            request,
            "htmx_components/insight_generation_result.html",
            {
                "entry": entry,
                "insight": insight,
            },
        )
