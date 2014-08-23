from django.conf.urls import patterns, include, url
from django.contrib import admin

from perforadora.views import HomeView
from perforadora.views import JSONInitView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', HomeView.as_view()),
    url(r'^modulos.json$', JSONInitView.as_view()),
    url(r'^app/', include('app_planillas.urls')),
    url(r'^admin/', include(admin.site.urls))
)
