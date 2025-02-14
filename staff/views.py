from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Employee
# Create your views here.

def staff(request):
    staff = Employee.objects.all()
    return render(request, 'staff.html', {'staff' : staff})

def employee_more(request, employee_id):
    if request.method == "GET":
        employee = get_object_or_404(Employee, id=employee_id)
        return render(request, 'employee_more.html', {'employee': employee})
    return Http404