from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=10)

class Tag(models.Model):
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=40, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='dishes', null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    photo = models.ImageField(upload_to='menu/', blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name="dishes", blank=True)

    def __str__(self):
        return self.name

