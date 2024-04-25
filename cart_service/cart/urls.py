from django.urls import path
from . import views

urlpatterns = [
	path('carts/', views.cart_list, name='view_carts_&_add_cart'),
	path('carts/<int:pk>', views.cart_detail, name='view_update_delete_cart'),

]