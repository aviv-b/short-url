from inspect import Attribute
from .models import Url
from django import forms

class UrlForm(forms.ModelForm):
    long_url = forms.CharField(label='',
                    max_length=100,
                    widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Url
        fields = ['long_url']