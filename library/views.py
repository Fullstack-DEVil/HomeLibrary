from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from integrations.open_library_api import OpenLibraryApi

# Create your views here.
def library(request):
    books = Book.objects.all().values()
    context = {
        'books': books,
    }
    return render(request, 'index.html', context)

def search_book_by_isbn(request):
    data = None

    if request.method == "POST":
        isbn = request.POST.get("isbn")
        api = OpenLibraryApi()
        data = api.search_by_isbn(isbn)

    context = {
        'data': data,
    }
    return render(request, 'index.html', context)