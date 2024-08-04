from rest_framework import serializers
from .models import ItemNews

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemNews
        fields = '__all__'
