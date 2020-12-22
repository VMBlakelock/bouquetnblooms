from django.shortcuts import render
from .models import Product

# product views


def all_products(request):
    """ View that shows all products, including sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
