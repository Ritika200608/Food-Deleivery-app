from django.urls import path
from . import views
from users.views import welcome  # Import the welcome view




from django.urls import path
from .views import restaurant_list, menu_view, cart_view, place_order, order_success

urlpatterns = [
    path('', restaurant_list, name='restaurant_list'),
    path('restaurants/<int:restaurant_id>/menu/', menu_view, name='menu'),
    path('cart/', cart_view, name='cart'),
    path('place_order/', place_order, name='place_order'),
    path('order_success/', order_success, name='order_success'),
    path('', welcome, name='welcome'),  # Make sure this matches your welcome view

]



