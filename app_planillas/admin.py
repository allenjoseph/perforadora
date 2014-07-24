from django.contrib import admin

from models import Ocupacion
class OcupacionAdmin(admin.ModelAdmin):
	list_display = (
		'id_ocupacion',
		'nombre'
	)
admin.site.register(Ocupacion, OcupacionAdmin)

from models import Categoria
class CategoriaAdmin(admin.ModelAdmin):
	list_display = (
		'idategoria',
		'nombre',
		'sueldo'
	)
admin.site.register(Categoria, CategoriaAdmin)

from models import Tasa
class TasaAdmin(admin.ModelAdmin):
	list_display = (
		'id_tasa',
		'referencia',
		'porcentaje'
	)
admin.site.register(Tasa, TasaAdmin)

from models import Seguro
class SeguroAdmin(admin.ModelAdmin):
	list_display = (
		'id_seguro',
		'tasa',
		'nombre'
	)
admin.site.register(Seguro, SeguroAdmin)

from models import Prestamo
class PrestamoAdmin(admin.ModelAdmin):
	list_display = (
		'id_prestamo',
		'trabajador',
		'monto',
		'fecha'
	)
admin.site.register(Prestamo, PrestamoAdmin)

from models import Letra
class LetraAdmin(admin.ModelAdmin):
	list_display = (
		'id_letra',
		'prestamo',
		'fecha'
	)
admin.site.register(Letra, LetraAdmin)

from models import Trabajador
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
admin.site.register(Trabajador, TrabajadorAdmin)

from models import Dia
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

from models import ReporteSemanal
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

from models import Parametro
class ParametroAdmin(admin.ModelAdmin):
    list_display = (
    	'id_parametro', 
    	'nombre',
    	'abreviatura'
	)
admin.site.register(Parametro, ParametroAdmin)