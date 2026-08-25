from django.urls import path
from . import views

urlpatterns = [
    path('library/', views.library, name='library'),
    path("search-book/", views.search_book_by_isbn, name="search_book_by_isbn"),
]