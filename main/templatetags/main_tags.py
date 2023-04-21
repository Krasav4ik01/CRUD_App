from django import template
from main.models import *

register = template.Library()

@register.inclusion_tag('main/simple.html')
def draw_menu():
    menu = MenuItem.objects.all()
    return {"menu": menu}
