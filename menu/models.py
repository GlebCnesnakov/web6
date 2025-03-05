from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=10)


class Dish(models.Model):
    name = models.CharField(max_length=40, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    photo = models.ImageField(upload_to='menu/', blank=True, null=True)

    def __str__(self):
        return self.name

