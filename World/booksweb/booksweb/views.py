from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book, Author, Genre
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render



def main_page(request):
    num_books = Book.objects.all().count()
    num_authors = Author.objects.count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    return render(
        request,
        'booksweb/main_page.html',
        context={
            'num_books': num_books,
            'num_authors': num_authors,
            'num_visits': num_visits
        },
    )


def contact_view(request):
    send_mail('Восстановление пароля', 'Books_Home', 'bookshomeworld@mail.ru', ['my_bisness@mail.ru'])


class BookListView(generic.ListView):
    model = Book
    paginate_by = 3


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 4





