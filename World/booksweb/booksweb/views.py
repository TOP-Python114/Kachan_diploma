from django.views.generic import ListView, DetailView
from .models import Book, Author, Genre, Language
from django.shortcuts import render
from .forms import AuthorForm
from django.http.response import HttpResponseRedirect, HttpResponseNotFound
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q


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

def author_add(request):
    return render(
        request,
        'booksweb/author_add.html',
        context={
            'form': AuthorForm(),
            'author': Author.objects.all()
        },
    )


def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        author = Author()
        author.first_name = request.POST.get('first_name')
        author.last_name = request.POST.get('last_name')
        author.date_of_birth = request.POST.get('date_of_birth')
        author.date_of_death = request.POST.get('date_of_death')
        author.foto_author = request.POST.get('foto_author')
        author.save()
        return HttpResponseRedirect('/author_add/')


def author_delete(request, id):
    try:
        author = Author.objects.get(id=id)
        author.delete()
        return HttpResponseRedirect('/author_add/')
    except Author.DoesNotExist:
        return HttpResponseNotFound("<h2>Автор не найден</h2>")


def author_edit(request, id):
    author = Author.objects.get(id=id)
    if request.method == 'POST':
        author.first_name = request.POST.get('first_name')
        author.last_name = request.POST.get('last_name')
        author.date_of_birth = request.POST.get('date_of_birth')
        author.date_of_death = request.POST.get('date_of_death ')
        author.save()
        return HttpResponseRedirect('/author_add/')
    else:
        return render(
            request,
            'booksweb/author_edit.html',
            context={
                'author': author
            }
        )


def book_update_delete(request):
    return render(
        request,
        'booksweb/book_update_delete.html',
        context={
            'current_url': request.path,
            'object_list': Book.objects.all(),
        },
    )


class BookListView(ListView):
    model = Book
    paginate_by = 8


class BookDetailView(DetailView):
    model = Book


class AuthorListView(ListView):
    model = Author
    paginate_by = 8


class BookCreate(CreateView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('book_update_delete')


class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('book_update_delete')


class BookDelete(DeleteView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('book_update_delete')

class SearchResultsView(ListView):
    model = Book
    template_name = 'book_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Book.objects.filter(
            Q(title__icontains=query) | Q(genre__name__icontains=query) | Q(author__last_name__icontains=query)
            | Q(author__first_name__icontains=query)
        )
        return object_list