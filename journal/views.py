from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from journal.forms import UserLoginForm
from journal.models import JournalEntry


class IndexView(generic.TemplateView):
    template_name = "landing.html"


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = "registration/login.html"


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


class JournalEntryListView(LoginRequiredMixin, generic.ListView):
    model = JournalEntry
    template_name = "journal/journal_entry_list.html"
    paginate_by = 10

    def get_queryset(self):
        return JournalEntry.objects.filter(user=self.request.user)
