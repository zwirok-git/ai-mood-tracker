from django.urls import path

from journal.features.account.views import (
    UserDetailView,
    UserUpdateView,
    UserDeleteView,
)

app_name = "account"


urlpatterns = [
    path("<int:pk>/", UserDetailView.as_view(), name="profile"),
    path("<int:pk>/edit/", UserUpdateView.as_view(), name="profile-edit"),
    path("<int:pk>/delete/", UserDeleteView.as_view(), name="profile-delete"),
]
