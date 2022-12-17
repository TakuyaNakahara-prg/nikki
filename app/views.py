from rest_framework import viewsets
from .serializers import NikkiSerializer
from .models import Nikki
# Create your views here.


class NikkiViewSet(viewsets.ModelViewSet):
    serializer_class = NikkiSerializer
    queryset = Nikki.objects.all()