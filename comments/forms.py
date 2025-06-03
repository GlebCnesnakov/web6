from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'image']

        widgets = {
            'text': forms.Textarea(attrs={
                'placeholder': 'Введите ваш комментарий...',
                'required': True,
                'class': 'comment-textarea'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'comment-file-input'
            }),
        }
