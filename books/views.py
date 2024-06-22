from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from books.models import BooksModel
from books.serializers import BooksSerializer
from rest_framework.views import APIView


class BookListAPIView(APIView):
    def get(self, request):
        books = BooksModel.objects.all()
        serializer = BooksSerializer(books, many=True)
        response = {
            'success': True,
            'total': books.count(),
            'books': serializer.data,

        }
        return Response(response, status=status.HTTP_200_OK)


class BookDetailAPIView(APIView):
    def get(self, request, pk):
        book = get_object_or_404(BooksModel, pk=pk)
        serializer = BooksSerializer(book)
        response = {
            'success': True,
            'book': serializer.data,

        }
        return Response(response, status=status.HTTP_200_OK)


class BookUpdateAPIView(APIView):
    def put(self, request, pk):
        book = get_object_or_404(BooksModel, pk=pk)
        serializer = BooksSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'success': True,
                'message': 'Book updated',
                'book': serializer.data
            }
            return Response(response, status=status.HTTP_202_ACCEPTED)
        else:
            response = {
                'success': False,
                'message': 'Invalid request',
                'errors': serializer.errors
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class BookCreateAPIView(APIView):
    def post(self, request):
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'success': True,
                'message': 'Book is created',
                'book': serializer.data
            }
            return Response(response)
        else:
            response = {
                'success': False,
                'message': 'Invalid request',
                'errors': serializer.errors
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class BookDeleteAPIView(APIView):
    def delete(self, request, pk):
        book = get_object_or_404(BooksModel, pk=pk)
        book.delete()
        response = {
            'success': True,
            'message': 'Book is deleted'
        }
        return Response(response, status=status.HTTP_204_NO_CONTENT)
