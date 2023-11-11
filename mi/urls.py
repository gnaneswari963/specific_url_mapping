from mi.views import *
from django.urls import path
app_name='anything'
urlpatterns=[
    path('rohith/',rohith,name='rohith'),
    path('siraj/',siraj,name='siraj'),
]