from django.conf.urls import handler404
from django.urls import path, register_converter
from . import views
from .converters import DishConverter
from django.http import HttpResponse, HttpResponseNotFound


urlpatterns = [
    path('', views.MenuListView.as_view(), name='menu'),
    path('<dish:dish>', views.DishDetailView.as_view(), name='dish_detail')

]

