"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import handler404
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse, HttpResponseNotFound
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Панель администрирования"
admin.site.index_title = "Ресторан"

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

handler404 = page_not_found


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('menu.urls')),
    path('comments/', include('comments.urls')),
    path('staff/', include('staff.urls')),
    path('vacancy/', include('vacancy.urls')),
    path('users/', include('users.urls', namespace='users'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
