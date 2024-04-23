from django import template

register = template.Library()


@register.filter(name='totalizer')
def totalizer(price, quantity):
    return price * quantity
