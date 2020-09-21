from django.shortcuts import render
# from django import forms
from myFapp import fo
# Create your views here.
def get_home_page(req):
    return render(req,'pages/home.html')
def get_form_page(req):
    myform=fo.UserForm()
    if req.method=='POST':
        myform=fo.UserForm(req.POST)
        if myform.is_valid():
            print('validation success!')
            print(myform.cleaned_data['name'])
            print(myform.cleaned_data['mail'])
            print(myform.cleaned_data['text'])
    return render(req,'pages/myforms.html', {'data':myform})
