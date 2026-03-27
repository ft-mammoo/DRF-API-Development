from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    page_query_param = 'page_num'
    max_page_size = 5

    def get_paginated_response(self, data):
        return Response({
            'links':{
                'next':self.get_next_link(),
                'previous': self.get_previous_link(),
            },
            'count': self.page.paginator.count,
            'size': self.page_size,
            'total_pages': self.page.paginator.num_pages,
            'results': data,
        })
