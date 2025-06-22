from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from ..models import Book
from ..serializers.drf_serializers import (
    BookListSerializers,
    BookRetrieveSerializers,
    BookCreateSerializers,
)
from rest_framework.decorators import action

class bookViewsets(viewsets.ModelViewSet):
    serializer_class = BookListSerializers
    # Selects all books
    queryset = Book.objects.all().order_by('-created_date')
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['title', 'author__name']
    ordering_fields = ['created_date', 'updated_date']
    lookup_field = 'public_id'
    filterset_fields = {
        'title': ['exact'],
        'published_date': ['exact', 'year__gt', 'year__lt'],
    }

# Get all books
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return BookCreateSerializers
        elif self.action == 'retrieve':
            return BookRetrieveSerializers
        return super().get_serializer_class()

    @action(detail=False, methods=['get'], name='action_name', url_path='action-url')
    def action_name(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
