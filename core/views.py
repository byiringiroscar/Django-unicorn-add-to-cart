from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.models import Product


# Create your views here.


@login_required
def cart(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'home.html', context)


def login(request):
    pass


def logout(request):
    pass
