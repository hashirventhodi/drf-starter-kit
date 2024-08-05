from rest_framework.pagination import PageNumberPagination

from utils.custom_response import CustomResponse
from rest_framework import status

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
    
    def get_paginated_response(self, data):
        page_size = self.get_page_size(self.request)
        result = {
            'items': data,
            'pagination': {
                'total': self.page.paginator.count,
                'count': len(data),
                'per_page': page_size,
                'current_page': self.page.number,
                'total_pages': self.page.paginator.num_pages
            }
        }
        return CustomResponse(data=result, status=status.HTTP_200_OK, message="Successfully fetched the data")
