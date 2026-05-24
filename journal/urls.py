from django.contrib.auth.views import LogoutView
from django.urls import path

from journal.views import (
    UserLoginView,
    UserDetailView,
    UserUpdateView,
    UserCreateView,
    IndexView,
    UserDeleteView,
    JournalEntryListView,
)

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("profile/<int:pk>/", UserDetailView.as_view(), name="profile"),
    path("profile/<int:pk>/edit/", UserUpdateView.as_view(), name="profile-edit"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", UserCreateView.as_view(), name="register"),
    path("", IndexView.as_view(), name="home"),
    path("profile/<int:pk>/delete/", UserDeleteView.as_view(), name="profile-delete"),
    path("journal/", JournalEntryListView.as_view(), name="journal-entry-list")

    # HTMX-urls
]