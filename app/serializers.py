from rest_framework import serializers
from .models import *
from rest_framework import filters

class AddressSerializer(serializers.Serializer):
    address=serializers.CharField()
    output_format=serializers.CharField()
