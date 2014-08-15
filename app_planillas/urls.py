from django.conf.urls import patterns, include, url

from app_planillas import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'ocupacion', views.OcupacionViewSet)

urlpatterns = patterns('',
    # Examples:
    url(r'^', include(router.urls))
)
