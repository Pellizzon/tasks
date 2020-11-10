from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getTasks', views.getTasks, name='AllTasks')
]
