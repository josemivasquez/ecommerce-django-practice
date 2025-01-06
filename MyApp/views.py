from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Person, Product, EventDetail, Event
from .carrito import Carrito

from datetime import datetime
from .views_folder.cart_views import *
from .views_folder.user_views import *

def home(request):
    return render(request, "home.html")

def index(request):
    return render(request, 'index.html')

def sale(request):
    cart = Carrito(request).cart
    event = Event(
        type = 'S',
        part_id = int(request.session['actual_user']),
        date = datetime.now(),
        amount = float(cart['total']),
    )
    event.save()
    
    for id, data in cart['products'].items():
        event_detail = EventDetail(
            event = event,
            product_id = int(id), 
            varProduct = -data['cantidad'],
            money = data['subtotal']
        )

        # Update product quantity
        product = Product.objects.get(id=id)
        product.quantity -= data['cantidad']
        product.save()
        
        event_detail.save()
    
    return redirect('/main/clean_cart')

def main(request):
    actual_dni = request.session.get('actual_user')
    actual_user = Person.objects.get(dni=actual_dni)
    catalog = Product.objects.all()
    cart = Carrito(request)
    
    return render(request, 'main.html', {
        'user' : actual_user,
        'catalog' : catalog, 
        'cart' : cart.cart,
    })

def sales_view(request):
    user_dni = request.session['actual_user']
    actual_user = Person.objects.get(dni=user_dni)
    sales = Event.objects.filter(type='S', part_id=user_dni)    
    return render(request, 'sales_view.html', {
        'sales' : sales,
        'user' : actual_user,
    })

def sale_detail(request, id):
    sale = Event.objects.get(id=id)
    details = EventDetail.objects.filter(event=sale)
    
    user = Person.objects.get(dni=request.session['actual_user'])
    
    return render(request, 'sale_detail.html', {
        'sale' : sale,
        'details' : details,
        'user' : user,
    })
    