from django.shortcuts import render
from django import forms
from my_forms_app import forms

# Create your views here.
def get_home_page(arg):
    return render(arg,'pages/home.html')

def get_form_page(arg):
    # logic for input output
    form=forms.MyFormPage()
    if arg.method=='POST':
        form=forms.MyFormPage(arg.POST)
        if form.is_valid():
            print('validation success')
            print(form.cleaned_data['name'])
            print(form.cleaned_data['mail'])
            print(form.cleaned_data['text'])
    return render(arg,'pages/forms.html',{'data':form})
