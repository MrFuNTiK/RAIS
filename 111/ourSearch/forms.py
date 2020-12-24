from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class URLForm(forms.ModelForm):

    class Meta:
        model = URLTable
        fields = ('urladress',)
        #widgets = {
        #    'urladress': forms.URLInput(attrs={'class': 'col-md-12 form-control'}),
        #}

class ParseForm(forms.ModelForm):
    
    class Meta:
        model = WORDSTable
        fields = ('word',)

class UpdForm(forms.ModelForm):
    class Meta:
        model = WORDSTable
        fields = ('word',)

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class DeleteURLForm(forms.Form):
    url = forms.URLField()
    class Meta:
        model = URLTable
        fields = ('urladress',)