from django.urls import path
from . import views

urlpatterns = [
    path ('order', views.all_order, name = 'Home/' ),
    path('update', views.update, name = 'update/')
    
]