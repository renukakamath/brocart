from django import template

register = template.Library()

@register.simple_tag(name='multiple')
def multiple(a, b):
    return a*b
 
