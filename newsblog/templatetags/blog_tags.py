from django import template
from newsblog.models import Category

register = template.Library()


@register.simple_tag()
def get_all_categories():
    categories = Category.objects.all()
    return categories
