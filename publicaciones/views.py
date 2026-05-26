from django.views.generic import TemplateView, ListView, DetailView
from .models import Publicacion

# ---------------------------------------------------------------------------
# InicioView
# ---------------------------------------------------------------------------
class InicioView(TemplateView):
    template_name = "publicaciones/inicio.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Bienvenido a nuestro Portal"
        context["mensaje"] = "Explorá las mejores publicaciones de nuestros autores."
        return context

# ---------------------------------------------------------------------------
# PublicacionListView
# ---------------------------------------------------------------------------
class PublicacionListView(ListView):
    model = Publicacion
    context_object_name = "publicacion_list"

# ---------------------------------------------------------------------------
# PublicacionDetailView
# ---------------------------------------------------------------------------
class PublicacionDetailView(DetailView):
    model = Publicacion
    context_object_name = "publicacion"
    pk_url_kwarg = "publicacion_id"