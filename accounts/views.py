from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import *


class RegisterPage(CreateView):
    template_name = 'accounts/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')
