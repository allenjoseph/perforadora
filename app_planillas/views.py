from django.views.generic import TemplateView

from models import Categoria

class PlanillaHomeView(TemplateView):
    template_name = "planilla_home.html"

    def get_context_data(self, **kwargs):
        context = super(PlanillaHomeView, self).get_context_data(**kwargs)
        context['page'] = 'planilla'
        context['categorias'] = Categoria.objects.all()
        return context

