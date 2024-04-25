from django.urls import path
from . import views

urlpatterns = [
	path('clothes-categories/', views.view_clothes_categories, name='view_categories_&_add_category'),
	path('clothes-categories/<int:pk>', views.clothes_category_detail, name='view_update_delete_category'),

	path('clothes/', views.view_clothes, name='view_clothess_&_add_clothes'),
	path('clothes/<str:pk>', views.clothes_detail, name='view_update_delete_clothes'),

]
