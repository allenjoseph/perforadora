from django.db import models

class Ocupacion(models.Model):
	id_ocupacion = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=200)
	class Meta:
		db_table = 'ocupacion'
	def __str__(self):
		return '%s' % (self.nombre)

class Categoria(models.Model):
	idategoria = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=200)
	sueldo = models.DecimalField(decimal_places=4, max_digits=10)
	class Meta:
		db_table = 'categoria'
	def __str__(self):
		return '%s' % (self.nombre)

class Tasa(models.Model):
	id_tasa = models.AutoField(primary_key=True)
	referencia = models.CharField(max_length=200)
	porcentaje = models.DecimalField(decimal_places=4, max_digits=10)
	class Meta:
		db_table = 'tasa'
	def __str__(self):
		return '%s' % (self.referencia)

class Seguro(models.Model):
	id_seguro = models.AutoField(primary_key=True)
	tasa = models.ForeignKey('Tasa', db_column='id_tasa')
	nombre = models.CharField(max_length=200)
	class Meta:
		db_table = 'trabajador_seguro'
	def __str__(self):
		return '%s' % (self.nombre)

class Prestamo(models.Model):
	id_prestamo = models.AutoField(primary_key=True)
	trabajador = models.ForeignKey('Trabajador', db_column='id_trabajador')
	monto = models.DecimalField(decimal_places=4, max_digits=10)
	fecha = models.DateTimeField()
	class Meta:
		db_table = 'prestamo'
	def __str__(self):
		return '%s - %s' % (self.id_prestamo, self.monto)

class Letra(models.Model):
	id_letra = models.AutoField(primary_key=True)
	prestamo = models.ForeignKey('Prestamo', db_column='id_prestamo')
	fecha = models.DateTimeField()
	class Meta:
		db_table = 'letra'
	def __str__(self):
		return '%s - %s' % (self.id_letra, self.fecha)

class Trabajador(models.Model):
	id_trabajador = models.AutoField(primary_key=True)
	nombres = models.CharField(max_length=200)
	apellido_paterno = models.CharField(max_length=200)
	apellido_materno = models.CharField(max_length=200)
	ind_asignacion_familiar = models.BooleanField(default=False)
	fecha_ingreso_planilla = models.DateTimeField()
	estado = models.ForeignKey('Parametro', db_column='id_estado')
	categoria = models.ForeignKey('Categoria', db_column='id_categoria')
	ocupacion = models.ForeignKey('Ocupacion', db_column='id_ocupacion')
	id_seguro_pension = models.ForeignKey('Seguro', db_column='id_seguro_pension', related_name='seguro_pension')
	id_seguro_salud = models.ForeignKey('Seguro', db_column='id_seguro_salud', related_name='seguro_salud')
	class Meta:
		db_table = 'trabajador'
	def __str__(self):
		return '%s %s %s' % (self.nombres, self.apellido_paterno, self.apellido_materno)

class Dia(models.Model):
	id_dia = models.AutoField(primary_key=True)
	nombre = models.ForeignKey('Parametro', db_column='id_nombre')
	fecha = models.DateTimeField()
	ind_dia_trabajado = models.BooleanField()
	ind_falta = models.BooleanField()
	ind_prestamo = models.BooleanField()
	ind_jornal = models.BooleanField()
	horas_normales = models.IntegerField()
	horas_extras = models.IntegerField()
	minutos_tardanza = models.IntegerField()
	trabajador = models.ForeignKey('Trabajador', db_column='id_trabajador')
	class Meta:
		db_table = 'dia'
	def __str__(self):
		return '%s' % (self.id_dia)

class ReporteSemanal(models.Model):
	id_reporte_semanal = models.AutoField(primary_key=True)
	trabajador = models.ForeignKey('Trabajador', db_column='id_trabajador')
	dias_trabajados = models.IntegerField()
	horas_normales = models.IntegerField()
	horas_extras = models.IntegerField()
	minutos_tardanza = models.IntegerField()
	dias_faltados = models.IntegerField()
	remuneracion_basica = models.DecimalField(decimal_places=4, max_digits=10)
	asignacion_familiar = models.DecimalField(decimal_places=4, max_digits=10)
	bonificacion = models.DecimalField(decimal_places=4, max_digits=10)
	otros_ingresos = models.DecimalField(decimal_places=4, max_digits=10)
	seguro_pension = models.DecimalField(decimal_places=4, max_digits=10)
	monto_letra = models.DecimalField(decimal_places=4, max_digits=10)
	otras_retenciones = models.DecimalField(decimal_places=4, max_digits=10)
	seguro_salud = models.DecimalField(decimal_places=4, max_digits=10)
	otros_aportes = models.DecimalField(decimal_places=4, max_digits=10)
	total_ingresos = models.DecimalField(decimal_places=4, max_digits=10)
	total_retenciones = models.DecimalField(decimal_places=4, max_digits=10)
	total_aportes = models.DecimalField(decimal_places=4, max_digits=10)
	neto_pagar = models.DecimalField(decimal_places=4, max_digits=10)
	fecha_inicial = models.DateTimeField()
	fecha_final = models.DateTimeField()
	class Meta:
		db_table = 'reporte_semanal'
	def __str__(self):
		return '%s' % (self.id_reporte_semanal)

class Parametro(models.Model):
	id_parametro = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=200)
	abreviatura = models.CharField(max_length=20)
	class Meta:
		db_table = 'parametro'
	def __str__(self):
		return '%s' % (self.nombre)
