from urllib.error import HTTPError
from .models import Dish, Tag, Reservation
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404
from django.views.defaults import page_not_found
from django.db.models import Q
from .forms import ReservationForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy
from utils import DataMixin
# def menu(request):
#     tags = Tag.objects.all()
#     selected_tags = request.GET.getlist('tags')
#     dishes = Dish.objects.all()
#     if selected_tags:
#         dishes = dishes.filter(tags__name__in=selected_tags)
#     form = ReservationForm()
#     if request.method == 'POST':
#         form = ReservationForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             try:
#                 #Reservation.objects.create(**form.cleaned_data)
#                 form.save()
#             except:
#                 form.add_error(None, 'Ошибка добавления поста')
#                 print(form.errors)
#         else:
#             print(form.errors)
    
#     context = {
#         'dishes': dishes,
#         'tags': tags,
#         'form': form
#     }
#     return render(request, 'menu.html', context)

# def dish_detail(request, dish):
#     dish_obj = get_object_or_404(Dish, name=dish)
#     return render(request, 'dish_detail.html', {'dish':dish_obj})

class MenuListView(DataMixin, FormMixin, ListView):
    model = Dish
    template_name = 'menu.html'
    context_object_name = 'dishes'
    form_class = ReservationForm
    success_url = reverse_lazy('menu')  # имя маршрута

    def get_queryset(self):
        queryset = super().get_queryset()
        selected_tags = self.request.GET.getlist('tags')
        if selected_tags:
            queryset = queryset.filter(tags__name__in=selected_tags).distinct()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, tags=Tag.objects.all())
        # context['tags'] = Tag.objects.all()
        # context['form'] = self.get_form()
        # return context

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        form = self.get_form()
        if form.is_valid():
            try:
                form.save()
            except Exception as e:
                form.add_error(None, 'Ошибка добавления брони')
        else:
            print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))


class DishDetailView(DataMixin, DetailView):
    model = Dish
    template_name = 'dish_detail.html'
    context_object_name = 'dish'
    slug_field = 'name'
    slug_url_kwarg = 'dish'


