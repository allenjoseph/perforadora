from django.conf.urls import patterns, include, url

from app_planillas.views import PlanillaHomeView

urlpatterns = patterns('',
    url(r'^$', PlanillaHomeView.as_view()),
)