from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from authors.models import AuthorsModels
from authors.serializers import AuthorsSerializer
from rest_framework.views import APIView


class AuthorListAPIView(APIView):
    def get(self, request):
        books = AuthorsModels.objects.all()
        serializer = AuthorsSerializer(books, many=True)
        response = {
            'success': True,
            'total': books.count(),
            'books': serializer.data,

        }
        return Response(response, status=status.HTTP_200_OK)


class AuthorDetailAPIView(APIView):
    def get(self, request, pk):
        book = get_object_or_404(AuthorsModels, pk=pk)
        serializer = AuthorsSerializer(book)
        response = {
            'success': True,
            'book': serializer.data,

        }
        return Response(response, status=status.HTTP_200_OK)


class AuthorsUpdateAPIView(APIView):
    def put(self, request, pk):
        book = get_object_or_404(AuthorsModels, pk=pk)
        serializer = AuthorsSerializer(book, data=request.data)
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


class AuthorsCreateAPIView(APIView):
    def post(self, request):
        serializer = AuthorsSerializer(data=request.data)
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


class AuthorsDeleteAPIView(APIView):
    def delete(self, request, pk):
        book = get_object_or_404(AuthorsModels, pk=pk)
        book.delete()
        response = {
            'success': True,
            'message': 'Book is deleted'
        }
        return Response(response, status=status.HTTP_204_NO_CONTENT)
