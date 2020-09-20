from django.shortcuts import render
#from django.core.urlresolvers import reverse_lazy # works on django 2
from django.urls import reverse_lazy #works on django 3
from django.views.generic import CreateView

from . import forms

# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
