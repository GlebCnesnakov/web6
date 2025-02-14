from django.conf.urls import handler404
from django.urls import path, register_converter
from . import views
from .converters import DishConverter
from django.http import HttpResponse, HttpResponseNotFound



urlpatterns = [
    path('', views.menu, name='menu'),
    # path('breakfast', views.breakfast),
    # path('breakfast/<slug:dish>/', views.breakfast_dish),
    # path('lunch', views.lunch),
    # path('lunch/<slug:dish>/', views.lunch_dish),
    # path('dinner', views.dinner),
    # path('dinner/<slug:dish>/', views.dinner_dish),
    path('<dish:dish>', views.dish_detail, name='dish_detail')

]

