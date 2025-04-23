from django.urls import path
from django.views.generic import TemplateView

app_name = "reportes"           #  ← namespace para reverse("reportes:listar")

urlpatterns = [
    # /reportes/  →  reverse("reportes:listar")
    path(
        "",
        TemplateView.as_view(template_name="stub.html"),  # vista provisional
        name="listar",
    ),
]
