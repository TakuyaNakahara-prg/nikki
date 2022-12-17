from rest_framework import serializers
from .models import Nikki

class NikkiSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y/%m/%d")
    class Meta:
        model = Nikki
        fields = ['id', 'title', 'content', 'created_at']