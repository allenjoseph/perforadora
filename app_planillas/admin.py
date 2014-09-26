from django.contrib import admin

from models import Ocupacion, Categoria, Tasa, Seguro, Prestamo, Letra, Trabajador, Dia, ReporteSemanal, Parametro

class OcupacionAdmin(admin.ModelAdmin):
	list_display = (
		'id_ocupacion',
		'nombre'
	)
admin.site.register(Ocupacion, OcupacionAdmin)

class CategoriaAdmin(admin.ModelAdmin):
	list_display = (
		'idategoria',
		'nombre',
		'sueldo'
	)
admin.site.register(Categoria, CategoriaAdmin)

class TasaAdmin(admin.ModelAdmin):
	list_display = (
		'id_tasa',
		'referencia',
		'porcentaje'
	)
admin.site.register(Tasa, TasaAdmin)

class SeguroAdmin(admin.ModelAdmin):
	list_display = (
		'id_seguro',
		'tasa',
		'nombre'
	)
admin.site.register(Seguro, SeguroAdmin)

class PrestamoAdmin(admin.ModelAdmin):
	list_display = (
		'id_prestamo',
		'trabajador',
		'monto',
		'fecha'
	)
admin.site.register(Prestamo, PrestamoAdmin)

class LetraAdmin(admin.ModelAdmin):
	list_display = (
		'id_letra',
		'prestamo',
		'fecha'
	)
admin.site.register(Letra, LetraAdmin)

class TrabajadorAdmin(admin.ModelAdmin):
    list_display = (
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
    list_filter = ('categoria','ocupacion')
    search_fields = ('nombres','apellido_paterno','apellido_materno')
admin.site.register(Trabajador, TrabajadorAdmin)

class DiaAdmin(admin.ModelAdmin):
    list_display = (
    	'id_dia',
		'nombre',
		'fecha',
		'ind_dia_trabajado',
		'ind_falta',
		'ind_prestamo',
		'ind_jornal',
		'horas_normales',
		'horas_extras',
		'minutos_tardanza',
		'trabajador'
	)
admin.site.register(Dia, DiaAdmin)

class ReporteSemanalAdmin(admin.ModelAdmin):
    list_display = (
    	'id_reporte_semanal',
		'trabajador',
		'dias_trabajados',
		'horas_normales',
		'horas_extras',
		'minutos_tardanza',
		'dias_faltados',
		'remuneracion_basica',
		'asignacion_familiar',
		'bonificacion',
		'otros_ingresos',
		'seguro_pension',
		'monto_letra',
		'otras_retenciones',
		'seguro_salud',
		'otros_aportes',
		'total_ingresos',
		'total_retenciones',
		'total_aportes',
		'neto_pagar',
		'fecha_inicial',
		'fecha_final'
	)
admin.site.register(ReporteSemanal,ReporteSemanalAdmin)

class ParametroAdmin(admin.ModelAdmin):
    list_display = (
    	'id_parametro',
    	'nombre',
    	'abreviatura'
	)
admin.site.register(Parametro, ParametroAdmin)
