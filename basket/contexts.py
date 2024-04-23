from django.shortcuts import get_object_or_404
from products.models import Product
from decimal import Decimal
from django.conf import settings


def basket_total(request):
    """
    This function returns a running total of items in the user's basket. It is
    based on the shopping bag function from the Boutique Ado project.
    """
    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})
    removed_products = []
    for id, quantity in basket.items():
        if Product.objects.filter(pk=id).exists():
            product = get_object_or_404(Product, pk=id)
            total += quantity * product.price
            product_count += quantity
            basket_items.append({
                'product_id': id,
                'quantity': quantity,
                'product': product
            })
        else:
            removed_products.append(id)
    for removed in removed_products:
        basket.pop(removed)
    request.session['basket'] = basket
    if total < settings.DELIVERY_LOWER_THRESHOLD:
        delivery_charge = settings.DELIVERY_LOWER_CHARGE
    elif total < settings.DELIVERY_HIGHER_THRESHOLD:
        delivery_charge = settings.DELIVERY_HIGHER_CHARGE
    else:
        delivery_charge = 0
    grand_total = round((Decimal(delivery_charge) + Decimal(total)), 2)
    context = {
        'delivery_charge': round(delivery_charge, 2),
        'free_remaining_amount': round(
            (Decimal(
                settings.DELIVERY_HIGHER_THRESHOLD - Decimal(total))), 2),
        'grand_total': grand_total,
        'basket_items': basket_items,
        'basket_total': total,
        'product_count': product_count
    }
    return context
