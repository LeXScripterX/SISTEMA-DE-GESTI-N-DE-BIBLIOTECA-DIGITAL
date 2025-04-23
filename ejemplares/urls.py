from django.urls import path
from django.views.generic import TemplateView

app_name = "ejemplares"    #  ←  namespace: reverse("ejemplares:listar")

urlpatterns = [
    # GET /ejemplares/ → reverse("ejemplares:listar")
    path(
        "",
        TemplateView.as_view(template_name="stub.html"),
        name="listar",
    ),
]
