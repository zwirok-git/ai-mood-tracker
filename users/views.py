from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import generic
from allauth.account.views import SignupView

from users.forms import UserLoginForm
from users.mixins import OwnerRequiredMixin, DemoRestrictedMixin


class UserDetailView(LoginRequiredMixin, OwnerRequiredMixin, generic.DetailView):
    model = get_user_model()
    template_name = "journal/user/user_detail.html"


class UserUpdateView(
    LoginRequiredMixin, OwnerRequiredMixin, DemoRestrictedMixin, generic.UpdateView
):
    model = get_user_model()
    fields = [
        "username",
        "first_name",
        "last_name",
        "email",
    ]
    template_name = "journal/user/user_update_form.html"
    success_url = "/"


class UserCreateView(SignupView):
    template_name = "registration/registration.html"


class UserDeleteView(
    LoginRequiredMixin, OwnerRequiredMixin, DemoRestrictedMixin, generic.DeleteView
):
    model = get_user_model()
    template_name = "journal/user/user_confirm_delete.html"
    success_url = reverse_lazy("home")


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = "registration/login.html"
