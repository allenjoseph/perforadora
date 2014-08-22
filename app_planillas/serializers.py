from models import Ocupacion
from rest_framework import serializers

class OcupacionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Ocupacion
		fields = ('id_ocupacion', 'nombre')
