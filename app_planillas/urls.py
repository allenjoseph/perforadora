from django.conf.urls import patterns, include, url

from app_planillas import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'ocupacion', views.OcupacionViewSet)
router.register(r'trabajador', views.TrabajadorViewSet)
router.register(r'categoria', views.CategoriaViewSet)
router.register(r'parametro', views.ParametroViewSet)
router.register(r'seguro', views.SeguroViewSet)
router.register(r'tasa', views.TasaViewSet)

urlpatterns = patterns('',
    # Examples:
    url(r'^', include(router.urls))
)
