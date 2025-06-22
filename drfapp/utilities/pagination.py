from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import LimitOffsetPagination

class myPageNumberPagination(PageNumberPagination):
    page_size = 10 
    page_query_param = 'page'
    page_size_query_param = 'size'
    max_page_size = 5000

class myLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 1000



