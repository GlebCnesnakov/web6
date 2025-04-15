from django.contrib import admin
from .models import Vacancy, Description
# Register your models here.

admin.site.register(Description)
@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('date', 'position', 'salary', 'description')
    list_display_links = ('salary', 'description')
    list_editable = ('position',)
    list_per_page = 10
    ordering = ('position',)
    search_fields = ('description',)
    list_filter = ('position',)
    readonly_fields = ('date',)