from rest_framework.pagination import (
LimitOffsetPagination,
PageNumberPagination
)

class AdvtLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 10



class AdvtPageNumberPagination(PageNumberPagination):
    page_size=3
    #Number of records which can be displayed in each page is the page_size

