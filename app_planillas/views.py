from models import Ocupacion, Trabajador, Categoria, Parametro, Seguro, Tasa
from serializers import OcupacionSerializer, TrabajadorSerializer, CategoriaSerializer, ParametroSerializer, SeguroSerializer, TasaSerializer
from rest_framework import viewsets

class OcupacionViewSet(viewsets.ModelViewSet):
	serializer_class = OcupacionSerializer
	queryset = Ocupacion.objects.all()

class TrabajadorViewSet(viewsets.ModelViewSet):
    serializer_class = TrabajadorSerializer
    queryset = Trabajador.objects.all()

class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()

class ParametroViewSet(viewsets.ModelViewSet):
    serializer_class = ParametroSerializer
    queryset = Parametro.objects.all()

class SeguroViewSet(viewsets.ModelViewSet):
    serializer_class = SeguroSerializer
    queryset = Seguro.objects.all()

class TasaViewSet(viewsets.ModelViewSet):
    serializer_class = TasaSerializer
    queryset = Tasa.objects.all()
