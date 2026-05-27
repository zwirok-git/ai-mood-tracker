from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import (
    UserDetailView,
    UserUpdateView,
    UserDeleteView,
    UserLoginView,
    UserCreateView,
    IndexView,
)

app_name = "account"


urlpatterns = [
    path("<int:pk>/", UserDetailView.as_view(), name="profile"),
    path("<int:pk>/edit/", UserUpdateView.as_view(), name="profile-edit"),
    path("<int:pk>/delete/", UserDeleteView.as_view(), name="profile-delete"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", UserCreateView.as_view(), name="register"),
    path("", IndexView.as_view(), name="home"),
]
