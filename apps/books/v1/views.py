from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils.decorators import method_decorator
from utils.decorators import has_permission
from utils.custom_response import CustomResponse
from utils.pagination import CustomPageNumberPagination
from ..models import Book
from .serializers import BookSerializer

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = CustomPageNumberPagination
    permission_classes = [IsAuthenticated]

    @method_decorator(has_permission('books.view_book'))
    def get(self, request, *args, **kwargs):
        books = self.get_queryset()
        page = self.paginate_queryset(books)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.serializer_class(books, many=True)
        return CustomResponse(data=serializer.data, status=status.HTTP_200_OK, message="Successfully fetched the data")

    @method_decorator(has_permission('books.add_book'))
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return CustomResponse(data=serializer.data, status=status.HTTP_200_OK, message="Successfully added")
        return CustomResponse(data=serializer.errors, message="Please provide valid data", status=status.HTTP_400_BAD_REQUEST)


class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    @method_decorator(has_permission('books.view_book'))
    def get(self, request, *args, **kwargs):
        book = self.get_object()
        serializer = self.serializer_class(book)
        return CustomResponse(data=serializer.data, status=status.HTTP_200_OK, message="Successfully fetched the data")

    @method_decorator(has_permission('books.change_book'))
    def put(self, request, *args, **kwargs):
        book = self.get_object()
        serializer = self.serializer_class(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return CustomResponse(data=serializer.data, status=status.HTTP_200_OK, message="Successfully updated")
        return CustomResponse(data=serializer.errors, message="Please provide valid data", status=status.HTTP_400_BAD_REQUEST)

    @method_decorator(has_permission('books.change_book'))
    def patch(self, request, *args, **kwargs):
        book = self.get_object()
        serializer = self.serializer_class(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return CustomResponse(data=serializer.data, status=status.HTTP_200_OK, message="Successfully updated")
        return CustomResponse(data=serializer.errors, message="Please provide valid data", status=status.HTTP_400_BAD_REQUEST)

    @method_decorator(has_permission('books.delete_book'))
    def delete(self, request, *args, **kwargs):
        book = self.get_object()
        book.delete()
        return CustomResponse(status=status.HTTP_204_NO_CONTENT, message="Successfully deleted")
