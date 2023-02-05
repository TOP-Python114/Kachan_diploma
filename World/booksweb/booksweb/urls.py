from django.conf import settings
from django.urls import path, re_path
from django.views.static import serve


from .views import main_page, author_add, author_create, author_delete,  author_edit, book_update_delete
from .views import BookListView, BookDetailView, AuthorListView
from .views import BookCreate, BookUpdate, BookDelete

urlpatterns = [
    path('', main_page, name='main_page'),
    path('author_add/', author_add, name='author_add'),
    path('book_update_delete/', book_update_delete, name='book_update_delete'),
    path('author_edit/<int:id>', author_edit, name='author_edit'),
    path('author_create/', author_create, name='author_create'),
    path('author_delete/<int:id>', author_delete, name='author_delete'),
    re_path(r'^book/create/$', BookCreate.as_view(), name='book_create'),
    re_path(r'^book/update/(?P<pk>\d+)$', BookUpdate.as_view(), name='book_update'),
    re_path(r'^book/delete/(?P<pk>\d+)$', BookDelete.as_view(), name='book_delete'),
    re_path(r'^books/$', BookListView.as_view(), name='books'),
    re_path(r'^book/(?P<pk>\d+)$', BookDetailView.as_view(), name='book_detail'),
    re_path(r'^authors/$', AuthorListView.as_view(), name='authors'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

]


