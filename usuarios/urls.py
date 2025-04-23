# usuarios/urls.py
from django.urls import path
from django.views.generic import TemplateView

app_name = "usuarios"          # ←  importantísimo para reverse("usuarios:listar")

urlpatterns = [
    # /usuarios/   →  reverse("usuarios:listar")
    path(
        "",
        TemplateView.as_view(template_name="stub.html"),  # vista provisional
        name="listar",
    ),
]
