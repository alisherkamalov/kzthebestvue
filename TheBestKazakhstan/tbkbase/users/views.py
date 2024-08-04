from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import CustomUser
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = ItemSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

