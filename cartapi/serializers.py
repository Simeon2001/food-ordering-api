from rest_framework import serializers
from .models import OrderItem

class order_serial (serializers.ModelSerializer):
    mea = serializers.ReadOnlyField(source='mea.name')
    class Meta:
        model = OrderItem
        fields = ['id','mea','order','quantity','get_total']
