from django.shortcuts import render, redirect
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
    context = {}

    if request.method == "POST":
        isbn = request.POST.get("isbn")
        api = OpenLibraryApi()
        data = api.search_by_isbn(isbn)

        if data is not None:
            cover_id = data["covers"][0]
            cover_url = f"https://covers.openlibrary.org/b/id/{cover_id}-L.jpg"

            context = {
                'data': data,
                'title': data['title'],
                'publish_date': data['publish_date'],
                'isbn': data['isbn_13'][0],
                'cover': cover_url,
            }
    return render(request, 'search_book.html', context)

def save_book(request):
    if request.method == "POST":
        Book.objects.create(
            title=request.POST.get("title"),
            publish_date=request.POST.get("publish_date"),
            isbn=request.POST.get("isbn"),
            cover_url=request.POST.get("cover_url"),
        )
    return redirect('library')