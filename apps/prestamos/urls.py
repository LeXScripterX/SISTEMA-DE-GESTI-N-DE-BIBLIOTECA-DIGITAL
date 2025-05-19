from django.urls import path
from django.views.generic import TemplateView

app_name = "prestamos"          #  ← namespace para reverse("prestamos:listar")

urlpatterns = [
    # /prestamos/  →  reverse("prestamos:listar")
    path(
        "",
        TemplateView.as_view(template_name="stub.html"),  # vista provisional
        name="listar",
    ),
]
