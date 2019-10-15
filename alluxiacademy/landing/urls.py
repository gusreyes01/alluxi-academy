from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_course, name='index'),
    path('cursos/<str:slug>', views.get_course, name='get_course'),    
]
