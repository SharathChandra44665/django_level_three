from django.urls import path
from my_forms_app import views
urlpatterns=[
    path('',views.get_form_page, name='get_form_page'),
]
