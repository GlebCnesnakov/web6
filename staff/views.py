from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Employee
from django.views.generic import ListView, DetailView, TemplateView
from utils import DataMixin
from django.contrib.auth.mixins import LoginRequiredMixin


class StaffListView(LoginRequiredMixin, DataMixin, TemplateView):
    template_name = 'staff.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['staff'] = Employee.objects.all()
        return context


class EmployeeDetailView(LoginRequiredMixin, DataMixin, DetailView):
    model = Employee
    template_name = 'employee_more.html'
    context_object_name = 'employee'
    slug_field = 'slug'         
    slug_url_kwarg = 'employee_slug'  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=context['employee'])