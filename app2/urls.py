from django.urls import path
from app2.views import *
app_name='reddy'

urlpatterns=[
    path('two/',two,name='two'),
]