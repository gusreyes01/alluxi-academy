from django.urls import path

from . import views

urlpatterns = [
    path('', views.introduccion_ds, name='index'),
    path('python-crash-course', views.python_crash_course, name='python_crash_course'),
    path('introduccion-data-science', views.introduccion_ds, name='introduccion_ds'),

]
