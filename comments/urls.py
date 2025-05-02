from django.conf.urls import handler404
from django.urls import path, register_converter
from . import views
from django.http import HttpResponse, HttpResponseNotFound


urlpatterns = [
    path('', views.comments, name='comments'),
    path('add/', views.add_comment, name='add_comment'),
    path('<int:comment_id>/edit', views.edit_comment, name='edit_comment'),
    path('<int:comment_id>/delete', views.delete_comment, name='delete_comment'),
]

