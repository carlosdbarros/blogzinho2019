import logging

from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http.response import HttpResponse, HttpResponseRedirect

from django.db.models import Q
from django.template.defaultfilters import slugify

from django.views.generic.base import View
from django.views.generic import (
    ListView, FormView, DetailView, 
    FormView,TemplateView, CreateView, 
    UpdateView, DeleteView
)

from .forms import AuthRegisterForm

class HomePageView(TemplateView):
    template_name = 'blog/index.html'


class AuthRegisterView(FormView):
    form_class = AuthRegisterForm
    template_name = 'registration/register.html'
    sucess_url = 'blog:login'

    def form_valid(self, form):
        if self.request.method == "POST":
            form = AuthRegisterForm(self.request.POST)
            if form.is_valid():
                form.save()
        else:
            form = AuthRegisterForm()

        return super(
            AuthRegisterView, self).form_valid(form)

    def get_success_url(self):
        return reverse(self.sucess_url)