from django.conf.urls import patterns, include, url

from app_planillas import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'ocupacion', views.OcupacionViewSet)
router.register(r'trabajador', views.TrabajadorViewSet)

urlpatterns = patterns('',
    # Examples:
    url(r'^', include(router.urls))
)
