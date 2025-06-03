from django.contrib import admin
from .models import Dish, Tag, Category


admin.site.register(Category)
admin.site.register(Tag)
# Register your models here.

class CategoryFilter(admin.SimpleListFilter):
    title = 'Категории'
    parameter_name = 'category__name'

    def lookups(self, request, model_admin):
        return [(category.id, category.name) for category in Category.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(category__id=self.value())
        return queryset

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'photo')
    list_display_links = ('name', 'category')
    list_per_page = 10
    search_fields = ('name__startswith',)
    list_filter = (CategoryFilter,)
    filter_horizontal = ('tags',)