from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None

    # Check if a get request exists
    if request.GET:
        # check if the category exists
        if 'category' in request.GET:
            # split into a list at the commas
            categories = request.GET['category'].split(',')
            # Filter down to products whos name is in the list
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
        # q is the name of the input in our search form
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            """ This variable is equal to a Q object where either
            the name or description contains the query."""
            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories
    }

    return render(request, 'products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'product_detail.html', context)
