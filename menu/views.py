from urllib.error import HTTPError
from .models import Dish, Tag, Reservation
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404
from django.views.defaults import page_not_found
from django.db.models import Q
from .forms import ReservationForm


def menu(request):
    tags = Tag.objects.all()
    selected_tags = request.GET.getlist('tags')
    dishes = Dish.objects.all()
    if selected_tags:
        dishes = dishes.filter(tags__name__in=selected_tags)
    form = ReservationForm()
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            try:
                #Reservation.objects.create(**form.cleaned_data)
                form.save()
            except:
                form.add_error(None, 'Ошибка добавления поста')
                print(form.errors)
        else:
            print(form.errors)
    
    context = {
        'dishes': dishes,
        'tags': tags,
        'form': form
    }
    return render(request, 'menu.html', context)

def dish_detail(request, dish):
    dish_obj = get_object_or_404(Dish, name=dish)
    return render(request, 'dish_detail.html', {'dish':dish_obj})
