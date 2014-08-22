from models import Ocupacion
from serializers import OcupacionSerializer
from rest_framework import viewsets

class OcupacionViewSet(viewsets.ModelViewSet):
	serializer_class = OcupacionSerializer
	queryset = Ocupacion.objects.all()