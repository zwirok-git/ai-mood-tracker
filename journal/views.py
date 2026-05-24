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




