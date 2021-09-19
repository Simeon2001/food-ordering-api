from django.test import TestCase

# Create your tests here.
from django.shortcuts import render
from .models import Order,OrderItem,Dropmeal
from order.models import Meal
from django.contrib.auth.models import User
from django.shortcuts import redirect
# Create your views here.
def cart (request):
    customer = request.user
    #print (customer)
    placed, created = Order.objects.get_or_create(customer=customer, complete=False)
    ##meal in orderitem by selected user
    item = placed.orderitem_set.all()
    print (item)
    cartItems = placed.get_cart_items
    cartTotal = placed.get_cart_total
    context = {'item':item,
    'cartItems':cartItems,
    'cartTotal':cartTotal
    }
    return render(request, 'cart.html', context)
    
def checkout(request):
    customer = request.user
    #print (customer)
    placed, created = Order.objects.get_or_create(customer=customer, complete=False)
    ####item in orderitem
    item = placed.orderitem_set.all()
    print (item)

    cartItems = placed.get_cart_items
    cartTotal = placed.get_cart_total
    context = {'item':item,
    'cartItems':cartItems,
    'cartTotal':cartTotal
    }
    return render(request, 'checkout.html', context)
    
def update (request):
    listen = request.POST.get('listen')
    no = listen[0]
    action = listen[-1]
    customer = request.user
    mea = Meal.objects.get(id=no)
    placed, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=placed, mea=mea)
    
    if action == 'Y':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'N':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    return redirect ('Home/')