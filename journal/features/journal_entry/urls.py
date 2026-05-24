from django.urls import path

from journal.features.journal_entry.views import (
    JournalEntryListView,
    JournalEntryCreateView,
    JournalEntryDetailView,
    JournalEntryUpdateView,
    JournalEntryDeleteView,
)


app_name = "journal"


urlpatterns = [
    path("journal/", JournalEntryListView.as_view(), name="journal-entry-list"),
    path("journal/entry/crete", JournalEntryCreateView.as_view(), name="entry-create"),
    path("journal/entry/<int:pk>/", JournalEntryDetailView.as_view(), name="entry"),
    path("journal/entry/<int:pk>/edit/", JournalEntryUpdateView.as_view(), name="entry-edit"),
    path("journal/entry/<int:pk>/delete/", JournalEntryDeleteView.as_view(), name="entry-delete"),
]



