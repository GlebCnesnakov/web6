from django.contrib import admin
from .models import Employee
# Register your models here.

@admin.register(Employee)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'description', 'photo', 'slug', 'description_characters_count')
    list_display_links = ('name',)
    list_editable = ('position',)
    list_per_page = 10
    ordering = ('position',)
    search_fields = ('description',)
    list_filter = ('position',)
    #readonly_fields = ('slug',)
    prepopulated_fields = {'slug': ('name',)}

    @admin.display(description='Символов в описании', ordering='position')
    def description_characters_count(self, emp: Employee):
        return len(emp.description)