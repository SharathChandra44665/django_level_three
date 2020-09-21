from django.shortcuts import render
from my_forms_app import forms
# Create your views here.
def get_home_page(arg):
    return render(arg,'pages/home.html')

def get_forms_page(arg):
    form=forms.FormName()
    if arg.method=='POST':
        form=forms.FormName(arg.POST)
        if form.is_valid():
            print('validation Success!!!')
            print('Name: '+form.cleaned_data['name'])
            print('mail: '+form.cleaned_data['mail'])
            print('Text-Area: '+form.cleaned_data['text'])


    return render(arg,'pages/myforms.html',{'form_val':form})
