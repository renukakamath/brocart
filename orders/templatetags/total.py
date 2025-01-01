from django import template

register = template.Library()

@register.simple_tag(name='totalamount')
def totalamount(cart):
    total = 0  # Initialize total before using it
    for item in cart.added_items.all():
        total += item.quantity * item.product.price
    return total

    
 