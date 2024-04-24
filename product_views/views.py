from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from datetime import datetime
from products.models import CheeseCategory, BeerCategory, Product
from user_account.models import Wishlist
from datetime import datetime, timedelta


def view_results(request):
    """
    Displays and filters a view allowing users to view and purchase
    various types of cheese or beer. Please note aspects of the search function
    are adapted directly from Boutique Ado, albeit in a highly modified state.
    """
    product_list = Product.objects.all()
    search_term = "all products"
    category = None
    type = None
    view = None
    sort = 'id'
    direction = 'desc'
    if request.GET:
        if 'view_category' in request.GET:
            view = "view_category=" + request.GET['view_category']
            values = request.GET['view_category'].split(',')
            type = values[0]
            if len(values) > 1:
                category = values[1]
                search_term = None
                if type == "cheese":
                    category = get_object_or_404(
                        CheeseCategory, pk=category)
                    product_list = Product.objects.filter(
                        cheese_category=category.id)
                else:
                    category = get_object_or_404(BeerCategory, pk=category)
                    product_list = Product.objects.filter(
                        beer_category=category.id)
            else:
                product_list = Product.objects.filter(product_type=type)
                category = None
                search_term = type
        if 'category' in request.GET:
            view = "category=" + request.GET['category']
            values = request.GET['category'].split(',')
            type = values[0]
            if len(values) > 1:
                category = values[1]
                search_term = None
                if type == "cheese":
                    product_list = Product.objects.filter(
                        cheese_category=category)
                    category = get_object_or_404(CheeseCategory, pk=category)
                else:
                    product_list = Product.objects.filter(
                        beer_category=category)
                    category = get_object_or_404(BeerCategory, pk=category)
            else:
                product_list = Product.objects.filter(product_type=type)
                category = None
                search_term = type
        if 'variety' in request.GET:
            products = Product.objects.all()
            view = "variety=" + request.GET['variety']
            variety = request.GET['variety'].replace("+", " ")
            search_term = variety
            query = variety.strip()
            queries = Q(
                        variety__icontains=query
                        )
            product_list = products.filter(queries)
        if 'query' in request.GET:
            products = Product.objects.all()
            view = "query=" + request.GET['query']
            query = request.GET['query'].strip()
            if query:
                queries = Q(
                    product_number__iexact=query
                    ) | Q(
                        name__icontains=query
                        ) | Q(
                            variety__icontains=query
                            ) | Q(
                                texture__icontains=query
                                )
                product_list = products.filter(queries)
                product_list_ids = []
                for product in product_list:
                    product_list_ids.append(product.id)
                search_term = query
                cheese_index = []
                cheese_query = Q(name__icontains=query)
                cheese_categories = CheeseCategory.objects.all().filter(
                    cheese_query)
                for category in cheese_categories:
                    cheese_index.append(category.id)
                for i in cheese_index:
                    index_query = Q(
                        cheese_category__exact=i
                    )
                    product = Product.objects.all().filter(index_query)
                    for id in product:
                        if id.id in product_list_ids:
                            continue
                        else:
                            try:
                                product_list = product_list | product
                            except UnboundLocalError:
                                product_list = product
                beer_index = []
                beer_query = Q(name__icontains=query)
                beer_categories = BeerCategory.objects.all().filter(beer_query)
                for category in beer_categories:
                    beer_index.append(category.id)
                for i in beer_index:
                    index_query = Q(
                        beer_category__exact=i
                    )
                    product = Product.objects.all().filter(index_query)
                    for id in product:
                        if id.id in product_list_ids:
                            continue
                        else:
                            try:
                                product_list = product_list | product
                            except UnboundLocalError:
                                product_list = product
            else:
                search_term = "all products"
                product_list = products
                category = None
            type = None
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'price':
                sortkey = 'price_per_amount'
            if sortkey == 'trending':
                sortkey = 'units_sold'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
        else:
            sortkey = "-id"
    product_list = product_list.order_by(sortkey)
    number = len(product_list)
    if number == 1:
        result = "result"
    else:
        result = "results"
    if request.user:
        wishlist_objects = Wishlist.objects.filter(user_id=request.user.id)
        wishlist = []
        for wish in wishlist_objects:
            wishlist.append(wish.product.id)
    template = 'product_views/view-products.html'
    current_sorting = f'{sort}_{direction}'
    context = {
        'wishlist': wishlist,
        'current_view': view,
        'number': number,
        'search_term': search_term,
        'products': product_list,
        'category': category,
        'result': result,
        'type': type,
        'current_sorting': current_sorting,
    }
    return render(request, template, context)


def product_detail(request, product_id):
    """
    Displays full details of a selected product, and also shows suggested
    pairings based on the cheese and beer category 'pairs with'
    many to many field.
    """
    product = get_object_or_404(Product, pk=product_id)
    if product.product_type == "beer":
        category = get_object_or_404(BeerCategory, name=product.beer_category)
        category_pairs = category.cheese.all()
        for category in category_pairs:
            try:
                pairings = pairings | Product.objects.filter(
                    cheese_category=category)
            except UnboundLocalError:
                pairings = Product.objects.filter(
                    cheese_category=category)
    else:
        category = get_object_or_404(
            CheeseCategory, name=product.cheese_category)
        category_pairs = category.pairs_with.all()
        pairings = Product.objects.filter(beer_category=0)
        for category in category_pairs:
            try:
                pairings = pairings | Product.objects.filter(
                    beer_category=category)
            except UnboundLocalError:
                pairings = Product.objects.filter(beer_category=category)
    if request.user:
        wishlist_objects = Wishlist.objects.filter(user_id=request.user.id)
        wishlist = []
        for wish in wishlist_objects:
            wishlist.append(wish.product.id)

    pairings = pairings.order_by('-units_sold')
    delivery_date = datetime.now().date() + timedelta(days=5)
    template = 'product_views/product-detail.html'
    context = {
        'wishlist': wishlist,
        'product': product,
        'pairings': pairings,
        'delivery_date': delivery_date,
    }
    return render(request, template, context)
