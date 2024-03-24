from products.models import CheeseCategory, BeerCategory

def menu_categories_and_user_status(request):
    """ Returns home page"""
    beer_categories=BeerCategory.objects.all().order_by('pk').values()
    cheese_categories=CheeseCategory.objects.all().order_by('pk').values()
    superuser = request.user.is_superuser
    authenticated = request.user.is_authenticated
    context = {
        'authenticated': authenticated,
        'superuser': superuser,
        'beer_categories': beer_categories,
        'cheese_categories': cheese_categories
    }
    return context