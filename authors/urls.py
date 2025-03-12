from django.urls import path
from . import views


urlpatterns = [
    path('authors/', views.AuthorListCreateView.as_view(), name='list'),
    path('authors/<int:pk>/', views.AuthorRetrieveUpdateDestroyView.as_view(), name='author_detail'),
    path('authors/<int:pk>/books/', views.AuthorBooksListView.as_view(), name='book_list'),
]