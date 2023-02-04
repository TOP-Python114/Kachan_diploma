from django.views import generic
from .models import Book, Author
from django.shortcuts import render
from .forms import AuthorsForm
from django.http.response import HttpResponseRedirect, HttpResponseNotFound


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


def authors_add(request):
    author = Author.objects.all()
    authorsform = AuthorsForm()
    return render(
        request,
        'booksweb/authors_add.html',
        context={
            'form': authorsform,
            'author': author
        },
    )


def authors_create(request):
    if request.method == 'POST':
        form = AuthorsForm(request.POST)
        if form.is_valid():
            author = Author()
            author.first_name = request.POST.get('first_name')
            author.last_name = request.POST.get('last_name')
            author.date_of_birth = request.POST.get('date_of_birth')
            author.date_of_death = request.POST.get('date_of_death ')
            author.save()
            return HttpResponseRedirect('/authors_add/')


def authors_delete(request, id):
    try:
        author = Author.objects.get(id=id)
        author.delete()
        return HttpResponseRedirect('/authors_add/')
    except Author.DoesNotExist:
        return HttpResponseNotFound("<h2>Автор не найден</h2>")


def authors_edit(request, id):
    author = Author.objects.get(id=id)
    if request.method == 'POST':
        author.first_name = request.POST.get('first_name')
        author.last_name = request.POST.get('last_name')
        author.date_of_birth = request.POST.get('date_of_birth')
        author.date_of_death = request.POST.get('date_of_death ')
        author.save()
        return HttpResponseRedirect('/authors_add/')
    else:
        return render(
            request,
            'booksweb/authors_edit.html',
            context={
                'author': author
            }
        )


class BookListView(generic.ListView):
    model = Book
    paginate_by = 3


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 4





