from django.urls import path
from books import views

urlpatterns = [
    path('create_book/', views.BookCreateView.as_view(), name='create-book'),
    path('list_of_books', views.BookListView.as_view(), name='list-of-books'),
    path('update_book/<int:pk>/', views.BookUpdateView.as_view(), name='update-books'),
    path('delete_book/<int:pk>/', views.BookDeleteView.as_view(), name='delete-books'),
    path('details_book/<int:pk>/', views.BookDetailView.as_view(), name='details-book')
]
