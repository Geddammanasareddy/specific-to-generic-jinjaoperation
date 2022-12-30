from django.urls import path
from app1.views import *
app_name="manasa"

urlpatterns=[
    path('one',one,name='one'),
]