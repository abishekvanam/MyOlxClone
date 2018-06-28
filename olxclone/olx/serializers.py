from rest_framework import serializers
from olx.models import *



class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model=Advertisement
        fields='__all__'
