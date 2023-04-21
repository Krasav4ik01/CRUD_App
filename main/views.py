from django.shortcuts import render, get_object_or_404

from django import template
from .models import MenuItem

register = template.Library()




def index(request):
    menu_items = MenuItem.objects.all()
    # var = {'menu_items': menu_items}
    return render(request, 'main/index.html', {'var': menu_items})


def show_detail(request, post_slug):
    post = get_object_or_404(MenuItem, url=post_slug)
    article = {'post':post}
    return render(request, 'main/details_view.html', context=article)