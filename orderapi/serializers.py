from rest_framework import serializers
from .models import Meal

class meal_serial (serializers.ModelSerializer):
    
    class Meta:
        model = Meal
        fields = ['id','category','name','price','available','image']
