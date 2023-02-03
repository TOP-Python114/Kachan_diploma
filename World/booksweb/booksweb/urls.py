
from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views

from .views import main_page, contact_view
from .views import BookListView, BookDetailView, AuthorListView

urlpatterns = [
    path('', main_page, name='main_page'),
    re_path(r'^books/$', BookListView.as_view(), name='books'),
    re_path(r'^book/(?P<pk>\d+)$', BookDetailView.as_view(), name='book_detail'),
    re_path(r'^authors/$', AuthorListView.as_view(), name='authors'),
    path('accounts/password/reset', contact_view, name='reset')

]


