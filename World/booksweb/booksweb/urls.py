from django.conf import settings
from django.urls import path, re_path
from django.views.static import serve

from .views import main_page
from .views import BookListView, BookDetailView, AuthorListView


urlpatterns = [
    path('', main_page, name='main_page'),
    re_path(r'^books/$', BookListView.as_view(), name='books'),
    re_path(r'^book/(?P<pk>\d+)$', BookDetailView.as_view(), name='book_detail'),
    re_path(r'^authors/$', AuthorListView.as_view(), name='authors'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT})


]


