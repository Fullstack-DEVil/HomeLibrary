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
    api = OpenLibraryApi()
    context = {}

    if request.method == "POST":
        isbn = request.POST.get("isbn")
        data_isbn = api.search_by_isbn(isbn)

        if data_isbn is not None:
            cover_url = None
            if data_isbn.get('covers'):
                cover_id = data_isbn["covers"][0]
                cover_url = f"https://covers.openlibrary.org/b/id/{cover_id}-L.jpg"

            description = data_isbn.get('description')
            if isinstance(description, dict):
                description = description.get('value')

            if not description and data_isbn.get('key'):
                data_olid = api.get_book_details_by_olid(data_isbn['key'])
                if data_olid is not None:
                    description = data_olid.get('description')
                    if isinstance(description, dict):
                        description = description.get('value')

            context = {
                'data': data_isbn,
                'title': data_isbn.get('title'),
                'isbn_10': data_isbn.get('isbn_10', [None])[0],
                'isbn_13': data_isbn.get('isbn_13', [None])[0],
                'description': description,
                'publish_date': data_isbn.get('publish_date'),
                'cover': cover_url,
            }
    return render(request, 'search_book.html', context)

def save_book(request):
    if request.method == "POST":
        Book.objects.create(
            title=request.POST.get("title"),
            isbn_10=request.POST.get("isbn_10"),
            isbn_13=request.POST.get("isbn_13"),
            description=request.POST.get("description"),
            publish_date=request.POST.get("publish_date"),
            cover_url=request.POST.get("cover_url"),
        )
    return redirect('library')