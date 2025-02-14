from django.urls import register_converter
from .models import Dish
from django.http import Http404

class DishConverter:
    regex = '[a-zA-Z]+'

    def to_python(self, value):
        if Dish.objects.filter(name=value).exists():
            return value
        return Http404()

    def to_url(self, value):
        return value

register_converter(DishConverter, 'dish')