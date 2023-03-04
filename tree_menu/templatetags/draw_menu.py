import datetime

from django import template

from tree_menu.models import Menu, MenuItem
from tree_menu.helpers import build_tree


register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, slug):
    full_path = context.request.get_full_path()
    try:
        menu = Menu.objects.get(slug=slug)
        items = MenuItem.objects.prefetch_related('children').filter(menu__slug=slug).all()
        return {'menu': menu, 'items': build_tree(items, full_path)}
    except Menu.DoesNotExist:
        return {'menu': '', 'items': []}





