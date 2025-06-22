import django_filters
from ..models import Book

class BookFilter(django_filters.FilterSet):
    max_pages = django_filters.NumberFilter(field_name='pages', lookup_expr='lte', help_text="Maximum number of pages")      
    min_pages = django_filters.NumberFilter(field_name='pages', lookup_expr='gte', help_text="Minimum number of pages")

    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'published_date', 'isbn']

