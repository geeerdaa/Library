from django.urls import path
from . import views


urlpatterns = [
    path('books_list/', views.book_list, name='book_list'),
    path('create/', views.create, name='create'),
    path('my_book/', views.my_book, name='my_book'),
    path('reader/', views.readers, name='reader')
    ]