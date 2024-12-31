from django import template

register = template.Library()

@register.filter(name='productsets')
def productsets(list_data, chunk_size):
    list_product = []
    i = 0
    for data in list_data:
        list_product.append(data)
        i = i + 1
        if i == chunk_size:
            yield list_product
            list_product = []
    if list_product:
        yield list_product
