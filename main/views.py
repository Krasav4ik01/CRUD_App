from django.shortcuts import render

# Create your views here.
from django import template
from django.urls import reverse
from .models import MenuItem
from django.http import request

register = template.Library()


def draw_menu(menu_name):
    menu_items = MenuItem.objects.filter(title=menu_name).select_related('parent')
    return _draw_menu_items(menu_items)


def _draw_menu_items(menu_items):
    result = ''
    for item in menu_items:
        # is_active = _is_item_active(item)
        is_active = True
        has_children = MenuItem.objects.filter(parent=item).exists()

        if is_active:
            result += f'<li class="active"><a href="{item.url}">{item.title}</a>'
            if has_children:
                result += '<ul>' + _draw_menu_items(MenuItem.objects.filter(parent=item))


def index(request):
    menu_items = MenuItem.objects.all()
    # var = {'menu_items': menu_items}
    return render(request, 'main/index.html', {'var': menu_items})