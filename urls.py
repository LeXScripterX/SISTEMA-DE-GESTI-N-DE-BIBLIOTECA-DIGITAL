from django.urls import path, include

urlpatterns = [
    path("usuarios/", include("usuarios.urls")),
    path("catalogo/", include("catalogo.urls")),
    path("ejemplares/", include("ejemplares.urls")),
    path("prestamos/", include("prestamos.urls")),
    path("reportes/", include("reportes.urls")),
]
