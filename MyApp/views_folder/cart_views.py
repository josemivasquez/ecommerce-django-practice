from ..models import Product
from ..carrito import Carrito
from django.shortcuts import redirect


def add_cart(request, id):
    cart = Carrito(request)
    product = Product.objects.get(id=id)
    cart.agregar(product)
    return redirect('/main')

def remove_cart(request, id):
    cart = Carrito(request)
    product = Product.objects.get(id=id)
    cart.eliminar(product)
    return redirect('/main')

def clean_cart(request):
    cart = Carrito(request)
    cart.limpiar()
    return redirect('/main')