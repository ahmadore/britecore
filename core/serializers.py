from .models import *
from rest_framework import serializers


class RiskSerializer(serializers.ModelSerializer):
    fields = serializers.JSONField()
    class Meta:
        model = Risk
        fields = "__all__"


class DataStoreSerializer(serializers.ModelSerializer):
    risk = RiskSerializer()
    data_dump = serializers.JSONField(binary=True)
    
    class Meta:
        model = DataStore
        fields = "__all__"