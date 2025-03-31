from urllib.error import HTTPError
from .models import Dish, Tag
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404
from django.views.defaults import page_not_found
from django.db.models import Q


def menu(request):
    tags = Tag.objects.all()
    selected_tags = request.GET.getlist('tags')
    dishes = Dish.objects.all()
    if selected_tags:
        dishes = Dish.objects.filter(tags__name__in=selected_tags)
    return render(request, 'menu.html', {'dishes':dishes, 'tags':tags})

def dish_detail(request, dish):
    dish_obj = get_object_or_404(Dish, name=dish)
    return render(request, 'dish_detail.html', {'dish':dish_obj})
