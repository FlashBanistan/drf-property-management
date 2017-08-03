from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
)
from rest_framework.filters import (
    DjangoFilterBackend,
    SearchFilter,
    OrderingFilter,
)



class DefaultsMixin(object):
    """
    Default settings for view authentication, permissions, filtering and
    pagination.
    """

    # authentication_classes = (
    #     JSONWebTokenAuthentication,
    # )
    #
    # permission_classes = (
    #     IsAuthenticated,
    # )

    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    )