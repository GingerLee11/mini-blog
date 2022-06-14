from dataclasses import fields
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.urls import reverse_lazy
from django.contrib import messages

from formtools.wizard.views import SessionWizardView

from .forms import BlogUserCreationForm


'''
class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = BlogUserCreationForm
    success_url = reverse_lazy('new-user-info')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url, kwargs=form.id)


class NewUserInformationView(UpdateView):
    """
    After registering with a username and password.
    The new user is asked to fill out additional information.
    """
    template_name = 'registration/new_user_info.html'
    form_class = NewUserInformationForm
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)
'''

class RegistrationView(CreateView):
    """
    Series of forms that take the user through the registration process.
    """
    template_name = 'registration/register.html'
    success_url = reverse_lazy('register-success')
    form_class = BlogUserCreationForm
    
