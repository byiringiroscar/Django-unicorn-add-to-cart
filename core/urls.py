from django.urls import path

from .views import *

urlpatterns = [
    path('', cart, name="cart"),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
]