from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

from app_planillas import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'ocupacion', views.OcupacionViewSet)

urlpatterns = patterns('',
    # Examples:

    url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls))
)
