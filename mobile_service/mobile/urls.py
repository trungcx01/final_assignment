from django.urls import path
from . import views

urlpatterns = [
	path('mobile-categories/', views.view_mobile_categories, name='view_categories_&_add_category'),
	path('mobile-categories/<int:pk>', views.mobile_category_detail, name='view_update_delete_category'),

	path('mobiles', views.view_mobile, name='view_mobiles_&_add_mobile'),
	path('mobiles/<str:pk>', views.mobile_detail, name='view_update_delete_mobile'),

]
