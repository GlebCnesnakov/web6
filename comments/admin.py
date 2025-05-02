from django.contrib import admin
from .models import Comment
from datetime import datetime
from django.utils.timesince import timesince
from django.utils import timezone
from django.utils.safestring import mark_safe
# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'is_active', 'date', 'passed_time', 'post_photo')
    list_display_links = ('text', 'date')
    list_editable = ('is_active',)
    list_per_page = 10
    ordering = ('-date',)
    actions = ['public', 'hide']
    search_fields = ('text__startswith',)
    list_filter = ('is_active', 'date')
    readonly_fields = ('date', 'post_photo')

    @admin.display(description='Изображение')
    def post_photo(self, comment: Comment):
        if comment.image:
            return mark_safe(f"<img src='{comment.image.url}'width=50>")
        return 'Нет изображения'

    @admin.display(description='Прошло с публикации', ordering='-date')
    def passed_time(self, comment: Comment):
        return (timezone.now() - comment.date)

    @admin.action(description='Опубликовать комментарии')
    def public(self, request, queryset):
        count = queryset.update(is_active=Comment.Status.PUBLISHED)
        self.message_user(request, f"Опубликовано {count} записи(ей).")

    @admin.action(description='Скрыть комментарии')
    def hide(self, request, queryset):
        count = queryset.update(is_active=Comment.Status.DRAFT)
        self.message_user(request, f"Скрыто {count} записи(ей).")
