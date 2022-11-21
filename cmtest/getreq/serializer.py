from .models import Getreq
from rest_framework import serializers


class GetReqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Getreq
        fields = '__all__'