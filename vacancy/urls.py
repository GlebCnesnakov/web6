from django.urls import path, register_converter
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.vacancy, name='vacancy'),
    path('<int:vacancy_id>/more', views.vacancy_more, name='vacancy_more')
]