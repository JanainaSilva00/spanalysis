from django.urls import path
from django.shortcuts import render

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('classroom', views.classroom, name='classroom'),
    path('classroom/courses', views.classroom_courses, name='classroom/courses'),
    path('classroom/account', views.classroom_account, name='classroom/account'),
    path('classroom/account_save', views.account_save, name='classroom/account_save'),
    path('classroom/classes', views.classes, name='classroom/classes'),
]