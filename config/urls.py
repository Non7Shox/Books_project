from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Library API",
      default_version='v1',
      description="Test description",
      terms_of_service="demo.com",
      contact=openapi.Contact(email="muhammadsodiqkasimov34@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny,],
)


urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    path('authors/', include('authors.urls')),
    path('users/', include('users.urls')),
]
