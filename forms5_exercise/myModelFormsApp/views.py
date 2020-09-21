from django.shortcuts import render
from myModelFormsApp.forms import NewUserForm
from django import forms
# Create your views here.
def get_home_page(req):
    return render(req,'pages/home.html')
def get_form_page(req):#1
    myform=NewUserForm()#2
    # return render(req,'pages/forms.html',{'data_form': myform})
    if(req.method=='POST'):#wait
        myform=NewUserForm(req.POST)
        if myform.is_valid():
            myform.save(commit=True)
            return get_home_page(req)
        else:
            print('something wrong happened')

    return render(req,'pages/forms.html',{'data_form': myform})#3
