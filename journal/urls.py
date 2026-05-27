from django.urls import path

from journal.views import (
    JournalEntryListView,
    JournalEntryCreateView,
    JournalEntryDetailView,
    JournalEntryUpdateView,
    JournalEntryDeleteView,
    GenerateInsightView,
    IndexView,
)

app_name = "journal"


urlpatterns = [
    path("journal/", JournalEntryListView.as_view(), name="journal-entry-list"),
    path("entry/create/", JournalEntryCreateView.as_view(), name="entry-create"),
    path("entry/<int:pk>/", JournalEntryDetailView.as_view(), name="entry"),
    path("entry/<int:pk>/edit/", JournalEntryUpdateView.as_view(), name="entry-edit"),
    path(
        "entry/<int:pk>/delete/", JournalEntryDeleteView.as_view(), name="entry-delete"
    ),
    path("", IndexView.as_view(), name="home"),
    # htmx-urls
    path(
        "<int:pk>/generate/",
        GenerateInsightView.as_view(),
        name="entry-generate-insight",
    ),
]
