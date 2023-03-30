from rest_framework import serializers
from .not_migrate import EmployeePhone


class EmployeePhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeePhone
        fields = ['ygdm', 'ygmc', 'sjhm', 'dhhm', 'bgdh']
