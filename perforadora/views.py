from django.views.generic import TemplateView
from django.views.generic import DetailView
from django import http
from django.utils import simplejson as json

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
    	context = super(HomeView, self).get_context_data(**kwargs)
    	context['page'] = 'home'
    	return context

#JSON Response Mixin
class JSONResponseMixin(object):
    def render_to_response(self, context):
        "Returns a JSON response containing 'context' as payload"
        return self.get_json_response(self.convert_context_to_json(context))

    def get_json_response(self, content, **httpresponse_kwargs):
        "Construct an `HttpResponse` object."
        return http.HttpResponse(content,
                                 content_type='application/json',
                                 **httpresponse_kwargs)

    def convert_context_to_json(self, context):
        "Convert the context dictionary into a JSON object"
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return json.dumps(context)

class JSONInitView(JSONResponseMixin, DetailView):
    def get(self, request, *args, **kwargs):
        modulos = [
        {
            'nombre' : 'HOME',
            'ruta' : '#/home'
        },
        {
            'nombre' : 'TRABAJADOR',
            'ruta' : '#/trabajador'
        },
        {
            'nombre' : 'PRESTAMO',
            'ruta' : '#/prestamo'
        },
        {
            'nombre' : 'DIA',
            'ruta' : '#/dia'
        },
        {
            'nombre' : 'SEMANA',
            'ruta' : '#/semana'
        },
        {
            'nombre' : 'PLANILLA' ,
            'ruta' : '#/planilla'
        } ]

        context = modulos
        return self.render_to_response(context)
