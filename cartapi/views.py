from django.shortcuts import render
from .models import Order,OrderItem,Dropmeal
from orderapi.models import Meal
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import order_serial

@api_view()
def all_order (request):
    customer = request.user
    permission_classes = (IsAuthenticated,)
    placed, created = Order.objects.get_or_create(customer=customer, complete=False)
    item = placed.orderitem_set.all()
    orderItems = placed.get_order_items
    orderTotal = placed.get_order_total
    context = {'orderItems':orderItems}
    serializer_class = order_serial(item,many=True)
#    serializer_class.is_valid()
    return Response(serializer_class.data)

@api_view(['POST'])
def update (request):
    customer = request.user
    if request.method == "POST":
        listen = request.data.get('listen')
        no = listen[0]
        action = listen[-1]
        mea = Meal.objects.get(id=no)
        placed, created = Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, created = OrderItem.objects.get_or_create(order=placed, mea=mea)
        
        if action == 'Y':
            orderItem.quantity = (orderItem.quantity + 1)
            orderItem.save()
            return Response (
                {
                    
                    "message": "add"
                }
            )
        elif action == 'N':
            orderItem.quantity = (orderItem.quantity - 1)
            orderItem.save()

            return Response (
                {
                    
                    "message": "minus"
                }
            )

        if orderItem.quantity <= 0:
            orderItem.delete()
            return Response (
                {
                    
                    "message": "None"
                }
            )
        