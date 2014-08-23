from models import Ocupacion, Trabajador
from serializers import OcupacionSerializer, TrabajadorSerializer
from rest_framework import viewsets

class OcupacionViewSet(viewsets.ModelViewSet):
	serializer_class = OcupacionSerializer
	queryset = Ocupacion.objects.all()

class TrabajadorViewSet(viewsets.ModelViewSet):
    serializer_class = TrabajadorSerializer
    queryset = Trabajador.objects.all()
