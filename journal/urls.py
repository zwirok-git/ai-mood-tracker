from django.contrib.auth.views import LogoutView
from django.urls import path

from journal.features.account.views import UserCreateView
from journal.views import UserLoginView, IndexView

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", UserCreateView.as_view(), name="register"),
    path("", IndexView.as_view(), name="home"),
    # HTMX-urls
]
