from models import Ocupacion, Trabajador, Categoria, Parametro, Seguro, Tasa
from rest_framework import serializers

class OcupacionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Ocupacion
		fields = ('url','id_ocupacion', 'nombre')

class TrabajadorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trabajador
        fields = (
            'url',
            'id_trabajador',
            'nombres',
            'apellido_paterno',
            'apellido_materno',
            'ind_asignacion_familiar',
            'fecha_ingreso_planilla',
            'estado',
            'categoria',
            'ocupacion',
            'id_seguro_pension',
            'id_seguro_salud'
            )

class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ('url','idategoria','nombre','sueldo',)

class ParametroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Parametro
        fields = ('url','d_parametro','nombre','abreviatura')

class SeguroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Seguro
        fields = ('url','id_seguro','tasa','nombre',)

class TasaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tasa
        fields = ('url','id_tasa','referencia','porcentaje',)

