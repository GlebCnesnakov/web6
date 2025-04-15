from django.contrib import admin
from .models import Comment
from datetime import datetime
from django.utils.timesince import timesince
from django.utils import timezone
# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'is_active', 'date', 'passed_time')
    list_display_links = ('text', 'date')
    list_editable = ('is_active',)
    list_per_page = 10
    ordering = ('-date',)
    actions = ['public', 'hide']
    search_fields = ('text__startswith',)
    list_filter = ('is_active', 'date')
    readonly_fields = ('date',)

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
