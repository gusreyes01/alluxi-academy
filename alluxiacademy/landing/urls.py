from django.urls import path

from . import views

urlpatterns = [
    path('', views.introduccion_ds, name='index'),
    path('cursos/python-crash-course', views.python_crash_course, name='python_crash_course'),
    path('cursos/introduccion-data-science', views.introduccion_ds, name='introduccion_ds'),
    path('cursos/introduccion-data-governance', views.introduccion_dg, name='introduccion_dg'),
]
