from django import forms
from django.forms import ModelForm
from .models import *

class URLForm(forms.ModelForm):
    #urladress = forms.URLField(max_length=200)

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