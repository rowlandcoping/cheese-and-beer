from django.shortcuts import get_object_or_404
from products.models import Product

def basket_total(request):
    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})
    for id, quantity in basket.items():
        product = get_object_or_404(Product, pk=id)
        total += quantity * product.price
        product_count += quantity
        basket_items.extend({
            'product_id': id,
            'quantity': quantity,
            'product': product
        })
    context = {
        'basket_items': basket_items,
        'basket_total': total,
        'product_count': product_count,
        'basket_items': basket_items
    }
    return context
