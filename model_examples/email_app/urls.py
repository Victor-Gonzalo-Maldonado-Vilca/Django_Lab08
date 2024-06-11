# Video 7 'Sending Emails in Django'

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index)
]
