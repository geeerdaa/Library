from django.shortcuts import render
from .models import Book, Readers


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


def create(request):
    if request.method == 'GET':
        if request.GET.get('title', None) and request.GET.get('author', None):
            post = Book()
            post.title = request.GET.get('title', None)
            post.author = request.GET.get('author', None)
            post.save()
        return render(request, 'create.html')
    else:
        return render(request, 'create.html')


def my_book(request):
    return render(request, 'my_book.html')


def readers(request):
    if request.method == 'GET':
        if request.GET.get('last_name', None) and request.GET.get('first_name', None) and request.GET.get('middle_name', None):
            post = Readers()
            post.last_name = request.GET.get('last_name', None)
            post.first_name = request.GET.get('first_name', None)
            post.middle_name = request.GET.get('middle_name', None)
            post.save()
        return render(request, 'create_reader.html')
    else:
        return render(request, 'create_reader.html')