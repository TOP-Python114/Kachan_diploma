from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from .models import Book, Author, Genre

def main_page(request):
    num_books = Book.objects.all().count()
    num_authors = Author.objects.count()
    num_visits = 0
    return render(
        request,
        'booksweb/main_page.html',
        context={
            'num_books': num_books,
            'num_authors': num_authors,
            'num_visits': num_visits
        },
    )

class BookListView(generic.ListView):
    model = Book


class BookDetailView(generic.DetailView):
    model = Book





