from django.contrib.auth import get_user_model
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


class UserDetailView(generic.DetailView):
    model = get_user_model()


class UserUpdateView(generic.UpdateView):
    model = get_user_model()
    fields = [
        "username",
        "first_name",
        "last_name",
        "email",

    ]
    template_name_suffix = "_update_form"
    success_url = "/"