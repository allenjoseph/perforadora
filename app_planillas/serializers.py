from models import Ocupacion, Trabajador
from rest_framework import serializers

class OcupacionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Ocupacion
		fields = ('id_ocupacion', 'nombre')

class TrabajadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trabajador
        fields = (
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
