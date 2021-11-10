from django.contrib import admin
from django.urls import include, path
from mainApp import views

urlpatterns = [
    path('', include('userAuth.urls')),
    path('', views.index, name="home"),
    path('productPage', views.productPage, name="prodctPage"),
    path('cart', views.CartPage, name='Cart'),
    path('addToCart', views.addToCart, name='addToCart'),
    path('address', views.AddAddress, name="AddAddress"),
    path('removeFromCart', views.deleteFromCart, name='deleteFromCart'),
    path('buy', views.buyNow, name="BuyNow")
]
