from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'author', 'image']

        widgets = {
            'text': forms.Textarea(attrs={
                'placeholder': 'Введите ваш комментарий...',
                'required': True,
                'class': 'comment-textarea'
            }),
            'author': forms.TextInput(attrs={
                'placeholder': 'Ваше имя',
                'required': True,
                'class': 'comment-author-input'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'comment-file-input'
            }),
        }
