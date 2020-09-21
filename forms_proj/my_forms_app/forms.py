from django import forms

class  FormName(forms.Form):
    """docstring for  FormName."""

    name=forms.CharField()
    mail=forms.EmailField()
    text=forms.CharField(widget=forms.Textarea)
