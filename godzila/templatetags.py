from django import template
from django.template import Template

register = template.Library()

@register.simple_tag(takes_context=True)
def create_tooman(price):
    return str(price) + ' تومان'