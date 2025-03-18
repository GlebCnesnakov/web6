from django.urls import path, register_converter
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.staff, name='staff'),
    path('<slug:employee_slug>/more', views.employee_more, name='employee_more')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)