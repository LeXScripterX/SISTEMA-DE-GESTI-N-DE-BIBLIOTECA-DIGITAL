"""
URL configuration for gestor_biblioteca_universitaria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("usuarios/",   include("apps.usuarios.urls")),
    path("catalogo/",   include("apps.catalogo.urls")),
    path("ejemplares/", include("apps.ejemplares.urls")),
    path("prestamos/",  include("apps.prestamos.urls")),
    path("reportes/",   include("apps.reportes.urls")),
    # path('api/auth/', include('usuarios.urls')),
    # path('api/catalogo/', include('catalogo.urls')),
    # path('api/prestamos/', include('prestamos.urls')),
    # path('api/ejemplares/', include('ejemplares.urls')),
    # path('api/reportes/', include('reportes.urls')),
    #  # Documentación
    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
