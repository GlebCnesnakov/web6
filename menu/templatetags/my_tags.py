from django import template
import random
from ..models import Dish

register = template.Library()

@register.simple_tag
def random_dish():
    return random.choice(Dish.objects.all())