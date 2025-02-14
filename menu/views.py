from urllib.error import HTTPError
from .models import Dish
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404
from django.views.defaults import page_not_found

# Create your views here.


# def menu(request):
#         return HttpResponse('<h1>Главная страница с меню</h1>')
#
# def dinner(request):
#     if request.GET:
#         dinner_dish(request, request.GET.get("name"))
#     return HttpResponse('<h1>Страница ужин</h1>')
#
# def dinner_dish(request, dish):
#      if dish in dishes:
#         return HttpResponse(f'<h1>Ужин. Блюдо {dish}</h1>')
#      raise Http404()
#
# def lunch(request):
#     if request.GET:
#         lunch_dish(request, request.GET.get("name"))
#     return HttpResponse('<h1>Страница обед</h1>')
#
# def lunch_dish(request, dish):
#         return HttpResponse(f'<h1>Обед. Блюдо {dish}</h1>')
#
# def breakfast(request):
#     if request.GET:
#         breakfast_dish(request, request.GET.get("name"))
#         return HttpResponse('<h1>Страница завтрак</h1>')
#
# def breakfast_dish(request, dish):
#         return HttpResponse(f'<h1>Завтрак. Блюдо {dish}</h1>')

def menu(request):
    dishes = Dish.objects.all()
    return render(request, 'menu.html', {'dishes':dishes})

def dish_detail(request, dish):
    dish_obj = get_object_or_404(Dish, name=dish)
    return render(request, 'dish_detail.html', {'dish':dish_obj})
