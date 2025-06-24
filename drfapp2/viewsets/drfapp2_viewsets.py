from rest_framework import viewsets 
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from ..models import Author
from ..serializers.drf2_serializers import AuthorSerializer
from rest_framework.permissions import AllowAny

class AuthorViewsets(viewsets.ModelViewSet):

    serializer_class = AuthorSerializer
    queryset = Author.objects.all().order_by('-created_date')
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['first_name', 'last_name']
    ordering_fields = ['created_date', 'updated_date']
    lookup_field = 'public_id'
    filterset_fields = {
        'first_name': ['exact'],
        'last_name': ['exact'],

    }
    permission_classes = [AllowAny]

    def get_queryset(self):
        return super().get_queryset()
    