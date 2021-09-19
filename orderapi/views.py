from django.shortcuts import render
from rest_framework import generics
from .models import Meal
from .serializers import meal_serial
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view()
def all_meal (request):
    permission_classes = (IsAuthenticated,)
    meal = Meal.objects.all()
    serializer_class = meal_serial(meal,many=True)
    return Response(serializer_class.data)