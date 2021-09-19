from django.urls import path
from . import views

urlpatterns = [
    path ('meal', views.all_meal, name = 'Home/' ),
    
]