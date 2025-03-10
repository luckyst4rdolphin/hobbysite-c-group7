from django.shortcuts import render
from .models import Product

def products(request):
    products = Product.objects.all()
    ctx = {
        "products": products
    }

    return render(request, "merch_list.html", ctx)

def product(request, pk):
    product = Product.objects.get(pk = pk)
    ctx = {
        "product": product,
    }

    return render(request, "merch_detail.html", ctx)