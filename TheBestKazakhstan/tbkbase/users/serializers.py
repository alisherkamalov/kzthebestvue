from rest_framework import serializers
from .models import CustomUser

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['fullname', 'password', 'phone', 'date', 'token', 'id']