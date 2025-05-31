from functools import reduce
from django.utils import timezone
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Comment
from .forms import CommentForm
# Create your views here.

# def comments(request):
#     form = CommentForm()
#     all_comments = Comment.published.all()

#     if request.method == 'POST':
#         form = CommentForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('comments')

#     return render(request, 'comments.html', {
#         'form': form,
#         'comments': all_comments,
#     })

# def add_comment(request):
#     if request.method == "POST":
#         text = request.POST["text"]
#         author = request.POST["author"]
#         Comment.objects.create(text=text, author=author, date=timezone.now())
#         return redirect('../../comments/')
#     raise Http404()

# def edit_comment(request, comment_id):
#     comment = get_object_or_404(Comment, id=comment_id)

#     if request.method == "POST":
#         comment.text = request.POST["text"]
#         comment.save()
#         return redirect('../../comments/')
#     return render(request, 'edit_comment.html', {'comment':comment})

# def delete_comment(request, comment_id):
#     comment = get_object_or_404(Comment, id=comment_id)
#     comment.delete()
#     return redirect('../../comments/')

from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.utils import timezone
from .models import Comment
from .forms import CommentForm
from utils import DataMixin
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin


class CommentListView(LoginRequiredMixin, DataMixin, FormMixin, ListView):
    model = Comment
    form_class = CommentForm
    template_name = 'comments.html'
    context_object_name = 'comments'

    def get_queryset(self):
        return Comment.published.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context)

    def get_success_url(self):
        return reverse_lazy('comments')

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        form = self.get_form()
        if form.is_valid():
            form.instance.date = timezone.now()  # если вручную нужно
            form.instance.author = request.user
            form.save()
            return redirect(self.get_success_url())
        return self.render_to_response(self.get_context_data(form=form))


class CommentUpdateView(LoginRequiredMixin, DataMixin, UpdateView):
    model = Comment
    fields = ['text']
    template_name = 'edit_comment.html'
    pk_url_kwarg = 'comment_id'

    def get_success_url(self):
        return reverse_lazy('comments')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title='Редактирование отзыва')

    def dispatch(self, request, *args, **kwargs):
        comment = self.get_object()
        if comment.author != request.user or not request.user.has_perm('comments.change_comment'):
            raise PermissionDenied("Вы не можете редактировать этот комментарий.")
        return super().dispatch(request, *args, **kwargs)


class CommentDeleteView(LoginRequiredMixin, DataMixin, DeleteView):
    model = Comment
    template_name = 'confirm_delete.html'  # можно создать шаблон
    pk_url_kwarg = 'comment_id'

    def get_success_url(self):
        return reverse_lazy('comments')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title='Удаление отзыва')

    def dispatch(self, request, *args, **kwargs):
        comment = self.get_object()
        if comment.author != request.user or not request.user.has_perm('comments.delete_comment'):
            raise PermissionDenied("Вы не можете удалить этот комментарий.")
        return super().dispatch(request, *args, **kwargs)
