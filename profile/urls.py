# profile/urls.py

from django.urls import path
from .views import profile_index

app_name = 'profile'

urlpatterns = [
    path('', profile_index, name='index'),
]
