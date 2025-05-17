from django.conf.urls import handler404
from django.urls import path, register_converter
from . import views
from django.http import HttpResponse, HttpResponseNotFound


urlpatterns = [
    path('', views.CommentListView.as_view(), name='comments'),
    path('add/', views.CommentListView.as_view(), name='add_comment'),
    path('<int:comment_id>/edit', views.CommentUpdateView.as_view(), name='edit_comment'),
    path('<int:comment_id>/delete', views.CommentDeleteView.as_view(), name='delete_comment'),
]

