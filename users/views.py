from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from users.models import UsersModel
from users.serializers import UsersSerializer
from rest_framework.views import APIView


class UsersListAPIView(APIView):
    def get(self, request):
        books = UsersModel.objects.all()
        serializer = UsersSerializer(books, many=True)
        response = {
            'success': True,
            'total': books.count(),
            'books': serializer.data,

        }
        return Response(response, status=status.HTTP_200_OK)


class UserDetailAPIView(APIView):
    def get(self, request, pk):
        book = get_object_or_404(UsersModel, pk=pk)
        serializer = UsersSerializer(book)
        response = {
            'success': True,
            'book': serializer.data,

        }
        return Response(response, status=status.HTTP_200_OK)


class UserUpdateAPIView(APIView):
    def put(self, request, pk):
        book = get_object_or_404(UsersModel, pk=pk)
        serializer = UsersSerializer(book, data=request.data)
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


class UserCreateAPIView(APIView):
    def post(self, request):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'success': True,
                'message': 'User is created',
                'user': serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            response = {
                'success': False,
                'message': 'Invalid request',
                'errors': serializer.errors
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class UserDeleteAPIView(APIView):
    def delete(self, request, pk):
        book = get_object_or_404(UsersModel, pk=pk)
        book.delete()
        response = {
            'success': True,
            'message': 'Book is deleted'
        }
        return Response(response, status=status.HTTP_204_NO_CONTENT)
