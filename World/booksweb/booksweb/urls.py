from django.conf import settings
from django.urls import path, re_path
from django.views.static import serve
from .views import main_page, authors_add, authors_create, authors_delete,  authors_edit
from .views import BookListView, BookDetailView, AuthorListView

urlpatterns = [
    path('', main_page, name='main_page'),
    path('authors_add/', authors_add, name='authors_add'),
    path('authors_edit/<int:id>', authors_edit, name='authors_edit'),
    path('authors_create/', authors_create, name='authors_create'),
    path('authors_delete/<int:id>', authors_delete, name='authors_delete'),
    re_path(r'^books/$', BookListView.as_view(), name='books'),
    re_path(r'^book/(?P<pk>\d+)$', BookDetailView.as_view(), name='book_detail'),
    re_path(r'^authors/$', AuthorListView.as_view(), name='authors'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

]


