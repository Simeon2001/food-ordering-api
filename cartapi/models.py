from django.db import models
from django.contrib.auth.models import User
from orderapi.models import Meal
# Create your models here.

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)
        
    @property
    def get_order_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total 

    @property
    def get_order_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    mea = models.ForeignKey(Meal, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    @property
    def get_total(self):
        total = self.mea.price * self.quantity
        return total

class Dropmeal (models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    
    street = models.CharField(max_length=200, null=False)
    
    city = models.CharField(max_length=200, null=False, default='Akure')
    
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.street