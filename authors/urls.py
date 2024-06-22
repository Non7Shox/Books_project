from django.urls import path

from authors.views import *

urlpatterns = [
    path('', AuthorListAPIView.as_view()),
    path('create/', AuthorsCreateAPIView.as_view()),
    path('<int:pk>/', AuthorDetailAPIView.as_view()),
    path('<int:pk>/update', AuthorsUpdateAPIView.as_view()),
    path('<int:pk>/delete', AuthorsDeleteAPIView.as_view()),
]
