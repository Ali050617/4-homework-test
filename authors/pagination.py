from rest_framework.pagination import PageNumberPagination


class AuthorListPagination(PageNumberPagination):
    page_size = 10


class AuthorBookPagination(PageNumberPagination):
    page_size = 8