from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import generic
from allauth.account.views import SignupView

from users.forms import UserLoginForm


class UserDetailView(LoginRequiredMixin, UserPassesTestMixin, generic.DetailView):
    model = get_user_model()
    template_name = "journal/user/user_detail.html"

    def test_func(self):
        return self.request.user == self.get_object()


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = get_user_model()
    fields = [
        "username",
        "first_name",
        "last_name",
        "email",
    ]
    template_name = "journal/user/user_update_form.html"
    success_url = "/"

    def test_func(self):
        return self.request.user == self.get_object()


class UserCreateView(SignupView):
    template_name = "registration/registration.html"


class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = get_user_model()
    template_name = "journal/user/user_confirm_delete.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        return self.request.user == self.get_object()


class IndexView(generic.TemplateView):
    template_name = "landing.html"


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = "registration/login.html"
