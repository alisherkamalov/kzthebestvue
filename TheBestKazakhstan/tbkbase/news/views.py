from django.shortcuts import render
from rest_framework import viewsets
from .models import ItemNews
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = ItemNews.objects.all()
    serializer_class = ItemSerializer


