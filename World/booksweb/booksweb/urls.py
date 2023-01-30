
from django.urls import path, re_path

from .views import main_page
from .views import BookListView, BookDetailView

urlpatterns = [
    path('', main_page, name='main_page'),
    re_path(r'^books/$', BookListView.as_view(), name='books'),
    re_path(r'^book/(?P<pk>\d+)$', BookDetailView.as_view(), name='book_detail'),

]


