from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination

class PageCustomPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = "size"
    page_query_param = "s"
    max_page_size = 50

class PageLimitPagination(LimitOffsetPagination):
     default_limit = 2
     max_limit = 30
     offset_query_param = "offset"
     limit_query_param = "limit"