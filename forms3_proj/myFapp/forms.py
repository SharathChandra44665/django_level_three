from django import forms
from django.core import  validators

def Check_for_Name(val):
    if val[0].lower()!='s':
        raise forms.ValidationError('First letter Should be in Capitat S, for eg: Sharath')

class RevForm(forms.Form):
    """docstring for ."""
    name=forms.CharField(validators=[Check_for_Name])
    mail=forms.EmailField()
    text=forms.CharField(widget=forms.Textarea)
    botcatcher=forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
