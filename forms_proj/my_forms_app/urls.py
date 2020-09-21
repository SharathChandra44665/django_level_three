from django.urls import path
from my_forms_app import views
urlpatterns=[
    path('',views.get_forms_page,name='get_forms_page'),
]
