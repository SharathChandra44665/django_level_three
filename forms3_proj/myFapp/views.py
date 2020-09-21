from django.shortcuts import render
from django import forms
from myFapp import forms
# Create your views here.
def get_home_page(arg):
    return render(arg,'pages/home.html')
def get_form_page(arg):
    myform=forms.RevForm()
    if arg.method=='POST':
        myform=forms.RevForm(arg.POST)
        if(myform.is_valid()):
            print('Validation Success')
            print(myform.cleaned_data['name'])
            print(myform.cleaned_data['mail'])
            print(myform.cleaned_data['text'])
    return render(arg,'pages/myforms.html',{'dataF':myform})
