from django.views.generic import ListView, DetailView, FormView, View
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from .models import Vacancy
from .forms import UploadFileForm
from utils import DataMixin
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import os


def handle_file_request(f):
    upload_dir = 'uploads'
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    name = f.name
    ext = ''

    if '.' in name:
        ext = name[name.rindex('.'):]
        name = name[:name.rindex('.')]
    suffix = str(uuid.uuid4())
    file_path = os.path.join(upload_dir, f"{name}_{suffix}{ext}")
    with open(file_path, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)


# class VacancyListView(LoginRequiredMixin, DataMixin, ListView):
#     model = Vacancy
#     template_name = 'vacancy.html'
#     context_object_name = 'vacancies'
#     form_class = UploadFileForm
#     success_url = reverse_lazy('vacancy')  # Название маршрута в urls.py
    

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return self.get_mixin_context(context)

#     def post(self, request, *args, **kwargs):
#         self.object_list = self.get_queryset()
#         form = self.get_form()
#         if form.is_valid():
#             handle_file_request(form.cleaned_data['file'])
#             return self.form_valid(form)
#         return self.form_invalid(form)

class VacancyListView(LoginRequiredMixin, DataMixin, FormView):
    template_name = 'vacancy.html'
    form_class = UploadFileForm
    success_url = reverse_lazy('vacancy')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vacancies'] = Vacancy.objects.all()
        context['is_paginated'] = True  # если ты не используешь пагинацию
        return self.get_mixin_context(context)

    def form_valid(self, form):
        self.handle_file_request(form.cleaned_data['file'])
        return super().form_valid(form)

class VacancyDetailView(LoginRequiredMixin, DataMixin, View):
    # model = Vacancy
    # template_name = 'vacancy_more.html'
    # context_object_name = 'vacancy'
    # pk_url_kwarg = 'vacancy_id'
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return self.get_mixin_context(context, title=context['vacancy'])
    def get(self, request, vacancy_id):
        vacancy = get_object_or_404(Vacancy, pk=vacancy_id)
        return render(request, 'vacancy_more.html', {'vacancy': vacancy})

