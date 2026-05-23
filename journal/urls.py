from django.urls import path

from journal.views import UserLoginView, UserDetailView, UserUpdateView

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("profile/<int:pk>/", UserDetailView.as_view(), name="profile"),
    path("profile/<int:pk>/edit/", UserUpdateView.as_view(), name="profile-edit"),
]