# menu/utils.py

menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Отзывы", 'url_name': 'comments'},
    {'title': "Сотрудники", 'url_name': 'staff'},
    {'title': "Меню", 'url_name': 'menu'},
    {'title': "Вакансии", 'url_name': 'vacancy'},
]

class DataMixin:
    title_page = None
    paginate_by = 2

    def get_mixin_context(self, context, **kwargs):
        if self.title_page:
            context['title'] = self.title_page

        context['menu'] = menu
        context.setdefault('cat_selected', None)
        context.update(kwargs)
        return context
