from collections import OrderedDict

from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.PageNumberPagination):
    page_size_query_param = "page_size"
    max_page_size = 100

    def get_page_size(self, request):
        if self.page_size_query_param:
            page_size = min(
                int(
                    request.query_params.get(self.page_size_query_param, self.page_size)
                ),
                self.max_page_size,
            )
            if page_size > 0:
                return page_size
            elif page_size == 0:
                return None
            else:
                pass
        return self.page_size

    def get_paginated_response(self, data):
        return Response(
            OrderedDict(
                [
                    ("count", self.page.paginator.count),
                    ("page_number", self.page.number),
                    ("next", self.get_next_link()),
                    ("previous", self.get_previous_link()),
                    ("results", data),
                ]
            )
        )


class FlexiblePagination(CustomPagination):
    pass
