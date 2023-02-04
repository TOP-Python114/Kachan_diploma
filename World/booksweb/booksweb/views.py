from django.views.generic import ListView, DetailView
from .models import Book, Author, Genre, Language
from django.shortcuts import render
from .forms import AuthorForm,BookModelForm
from django.http.response import HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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
    author = Author.objects.all()
    authorform = AuthorForm()
    return render(
        request,
        'booksweb/author_add.html',
        context={
            'form': authorform,
            'author': author
        },
    )


def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = Author()
            author.first_name = request.POST.get('first_name')
            author.last_name = request.POST.get('last_name')
            author.date_of_birth = request.POST.get('date_of_birth')
            author.date_of_death = request.POST.get('date_of_death ')
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

#
# def book_add(request):
#     book = Book.objects.all()
#     bookform = BookForm()
#     return render(
#         request,
#         'booksweb/book_add.html',
#         context={
#             'form': bookform,
#             'book': book
#         },
#     )
#
#
# def book_create(request, pk:int):
#     if request.method == 'POST':
#         book = Book()
#         title = request.POST.get('title')
#         genre = request.POST.get('genre')
#         language = request.POST.get('language')
#         author = request.POST.getlist('author')
#         summary = request.POST.get('summary')
#         isn = request.POST.get('isn')
#         file = request.POST.get('file')
#         instance = Book(
#             id=pk,
#             title=title,
#             genre=Genre.objects.get(name=genre),
#             language=Language.objects.get(name=language),
#             author=Author.objects.get(first_name=author),
#             summary=summary,
#             isn=isn,
#             file=file
#         )
#         instance.save()
#         return HttpResponseRedirect('/book_add/')
#
#
# def book_delete(request, id):
#     try:
#         book = Book.objects.get(id=id)
#         book.delete()
#         return HttpResponseRedirect('/book_add/')
#     except Book.DoesNotExist:
#         return HttpResponseNotFound("<h2>Книга не найдена</h2>")
#
#
# def book_edit(request, id):
#     book = Book.objects.get(id=id)
#     if request.method == 'POST':
#         book.title = request.POST.get('title')
#         book.genre = request.POST.get('genre')
#         book.language = request.POST.get('language')
#         book.author = request.POST.get('author')
#         book.summary = request.POST.get('summary')
#         book.isn = request.POST.get('isn')
#         book.file = request.POST.get('file')
#         book.save()
#         return HttpResponseRedirect('/book_add/')
#     else:
#         return render(
#             request,
#             'booksweb/book_edit.html',
#             context={
#                 'book': book
#             }
#         )
#

class BookListView(ListView):
    model = Book
    paginate_by = 3


class BookDetailView(DetailView):
    model = Book


class AuthorListView(ListView):
    model = Author
    paginate_by = 4


class BookCreate(CreateView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('books')


class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('books')


class BookDelete(DeleteView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('books')

