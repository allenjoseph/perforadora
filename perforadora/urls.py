from django.conf.urls import patterns, include, url
from django.contrib import admin

from perforadora.views import HomeView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', HomeView.as_view()),
    url(r'^planilla/', include('app_planillas.urls')),
    url(r'^admin/', include(admin.site.urls))
)
