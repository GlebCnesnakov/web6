from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Employee
from django.views.generic import ListView, DetailView
from utils import DataMixin
# Create your views here.

# def staff(request):
#     staff = Employee.objects.all()
#     return render(request, 'staff.html', {'staff' : staff})

# def employee_more(request, employee_slug):
#     if request.method == "GET":
#         employee = get_object_or_404(Employee, slug=employee_slug)
#         return render(request, 'employee_more.html', {'employee': employee})
#     return Http404

class StaffListView(DataMixin, ListView):
    model = Employee
    template_name = 'staff.html'
    context_object_name = 'staff'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title='Сотрудники')


class EmployeeDetailView(DataMixin, DetailView):
    model = Employee
    template_name = 'employee_more.html'
    context_object_name = 'employee'
    slug_field = 'slug'         
    slug_url_kwarg = 'employee_slug'  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=context['employee'])