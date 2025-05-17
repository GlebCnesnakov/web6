from django.urls import path, register_converter
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.VacancyListView.as_view(), name='vacancy'),
    path('<int:vacancy_id>/more', views.VacancyDetailView.as_view(), name='vacancy_more')
]