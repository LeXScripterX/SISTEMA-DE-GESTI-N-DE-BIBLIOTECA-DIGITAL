from django.urls import path
from django.views.generic import TemplateView

app_name = "catalogo"      #  ←  namespace: reverse("catalogo:listar")

urlpatterns = [
    # GET /catalogo/  →  reverse("catalogo:listar")
    path(
        "",
        TemplateView.as_view(template_name="stub.html"),
        name="listar",
    ),
]
