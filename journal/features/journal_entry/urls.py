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
    path("", JournalEntryListView.as_view(), name="journal-entry-list"),
    path("entry/create/", JournalEntryCreateView.as_view(), name="entry-create"),
    path("entry/<int:pk>/", JournalEntryDetailView.as_view(), name="entry"),
    path("entry/<int:pk>/edit/", JournalEntryUpdateView.as_view(), name="entry-edit"),
    path("entry/<int:pk>/delete/", JournalEntryDeleteView.as_view(), name="entry-delete"),
]



