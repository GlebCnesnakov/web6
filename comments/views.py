from functools import reduce
from django.utils import timezone
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Comment
from .forms import CommentForm
# Create your views here.

def comments(request):
    form = CommentForm()
    all_comments = Comment.published.all()

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('comments')

    return render(request, 'comments.html', {
        'form': form,
        'comments': all_comments,
    })

def add_comment(request):
    if request.method == "POST":
        text = request.POST["text"]
        author = request.POST["author"]
        Comment.objects.create(text=text, author=author, date=timezone.now())
        return redirect('../../comments/')
    raise Http404()

def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == "POST":
        comment.text = request.POST["text"]
        comment.save()
        return redirect('../../comments/')
    return render(request, 'edit_comment.html', {'comment':comment})

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect('../../comments/')