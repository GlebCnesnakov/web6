from django.shortcuts import render, get_object_or_404, redirect
from .models import Vacancy
# Create your views here.

def vacancy(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'vacancy.html', {'vacancies' : vacancies})

def vacancy_more(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, id=vacancy_id)
    return render(request, 'vacancy_more.html', {'vacancy': vacancy})
