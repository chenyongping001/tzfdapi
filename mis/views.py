from .pagination import DefaultPagination
from .not_migrate import EmployeePhone
from .serializers import EmployeePhoneSerializer
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.core.cache import cache


class EmployeePhoneViewSet(viewsets.ReadOnlyModelViewSet):
    key = 'mis_employeephone_list'
    if cache.get(key) is None:
        data = EmployeePhone.objects.using('mis').all()
        cache.set(key, data, 1440*60)
    queryset = cache.get(key)
    serializer_class = EmployeePhoneSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['ygmc', 'sjhm']
    search_fields = ['ygdm', 'ygmc', 'sjhm', 'dhhm', 'bgdh']
    ordering_fields = ['ygdm', 'ygmc']
    pagination_class = DefaultPagination
