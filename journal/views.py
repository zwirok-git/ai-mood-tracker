from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from journal.forms import UserLoginForm


class IndexView(generic.TemplateView):
    template_name = "landing.html"


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = "registration/login.html"