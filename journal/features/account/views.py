from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import generic

from journal.forms import UserLoginForm


class UserDetailView(LoginRequiredMixin, UserPassesTestMixin, generic.DetailView):
    model = get_user_model()

    def test_func(self):
        return  self.request.user == self.get_object()


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = get_user_model()
    fields = [
        "username",
        "first_name",
        "last_name",
        "email",

    ]
    template_name_suffix = "_update_form"
    success_url = "/"

    def test_func(self):
        return  self.request.user == self.get_object()

class UserCreateView(generic.CreateView):
    pass


class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = get_user_model()
    success_url = reverse_lazy("home")

    def test_func(self):
        return  self.request.user == self.get_object()