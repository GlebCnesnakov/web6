from urllib.error import HTTPError
from .models import Dish, Tag, Reservation, DishReaction, DishReview
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.defaults import page_not_found
from django.db.models import Q
from .forms import ReservationForm, DishReviewForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy
from utils import DataMixin


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dish = self.object
        user = self.request.user

        context['form'] = DishReviewForm()
        context['reviews'] = dish.reviews.all().order_by('-date')
        context['likes'] = dish.reactions.filter(type='like').count()
        context['dislikes'] = dish.reactions.filter(type='dislike').count()
        context['user_reaction'] = None

        if user.is_authenticated:
            context['user_reaction'] = DishReaction.objects.filter(dish=dish, user=user).first()

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        user = request.user

        if not user.is_authenticated:
            return redirect('users:login')

        if 'review' in request.POST:
            form = DishReviewForm(request.POST)
            if form.is_valid():
                review, created = DishReview.objects.get_or_create(user=user, dish=self.object)
                review.text = form.cleaned_data['text']
                review.save()
        elif 'reaction' in request.POST:
            reaction_type = request.POST.get('reaction')
            if reaction_type in ['like', 'dislike']:
                reaction, created = DishReaction.objects.get_or_create(user=user, dish=self.object)
                reaction.type = reaction_type
                reaction.save()

        return redirect(self.request.path)



