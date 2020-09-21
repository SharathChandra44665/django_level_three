from django import forms
from myModelFormsApp.mydb_models import WebUsers
class NewUserForm(forms.ModelForm):
    # mail=forms.CharField(label='TestField') #not required. but check why?
    class Meta:
        model=WebUsers
        fields="__all__"
