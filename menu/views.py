from urllib.error import HTTPError
from .models import Dish
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404
from django.views.defaults import page_not_found

# Create your views here.

def menu(request):
    dishes = Dish.objects.all()
    print(dishes)
    return render(request, 'menu.html', {'dishes':dishes})

def dish_detail(request, dish):
    dish_obj = get_object_or_404(Dish, name=dish)
    return render(request, 'dish_detail.html', {'dish':dish_obj})
