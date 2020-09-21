from django.urls import path
from myModelFormsApp import views
urlpatterns = [
    path('', views.get_form_page,name='get_form_page'),
]
