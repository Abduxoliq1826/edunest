from django.urls import path
from .views import *
from panel.views import *
urlpatterns = [
    path('', dashboard, name='index'),
    path('mock', mock, name='mocks'),
    path('success', success, name='success'),
    path('addstudent/', addstudent, name='addstudent'),
    path('addstudent_mock/', addstudent_mock, name='addstudent_mock'),

    ]