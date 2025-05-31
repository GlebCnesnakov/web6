from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    

class Tag(models.Model):
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

class Dish(models.Model):
    name = models.CharField(max_length=40, unique=True, verbose_name='Название')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='dishes', null=True, verbose_name='Категория')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')
    photo = models.ImageField(upload_to='menu/', blank=True, null=True, verbose_name='Фото')
    tags = models.ManyToManyField(Tag, related_name="dishes", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"


class DishReview(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Отзыв')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('dish', 'user')


class DishReaction(models.Model):
    class Reaction(models.TextChoices):
        LIKE = 'like', 'Лайк'
        DISLIKE = 'dislike', 'Дизлайк'

    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='reactions')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    type = models.CharField(max_length=7, choices=Reaction.choices)

    class Meta:
        unique_together = ('dish', 'user')


class Reservation(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    guests = models.IntegerField()
    time = models.TimeField()
    agree = models.BooleanField()