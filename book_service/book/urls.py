from django.urls import path
from . import views

urlpatterns = [
	path('book-categories/', views.view_categories, name='view_categories_&_add_category'),
	path('book-categories/<int:pk>', views.category_detail, name='view_update_delete_category'),

	path('authors/', views.view_authors, name='view_author_&_add_author'),
	path('authors/<int:pk>', views.author_detail, name='view_update_delete_author'),

    path('publishers/', views.view_publishers, name='view_publisher_&_add_publisher'),
	path('publishers/<int:pk>', views.publisher_detail, name='view_update_delete_publisher'),


	path('books', views.view_books, name='view_books_&_add_book'),
	path('books/<str:pk>', views.book_detail, name='view_update_delete_book'),
	path('books', views.view_books, name='view_books_&_add_book'),

]
