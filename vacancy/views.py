from django.shortcuts import render, get_object_or_404, redirect
from .models import Vacancy
from .forms import UploadFileForm
import uuid
import os
# Create your views here.

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


def vacancy(request):
    vacancies = Vacancy.objects.all()
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_file_request(form.cleaned_data['file'])
    else:
        form = UploadFileForm()
    return render(request, 'vacancy.html', {'vacancies' : vacancies, 'form': form})

def vacancy_more(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, id=vacancy_id)
    return render(request, 'vacancy_more.html', {'vacancy': vacancy})

