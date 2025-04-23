import pytest
from django.urls import reverse

@pytest.mark.django_db
@pytest.mark.parametrize("url_name", [
    "usuarios:listar",          
    "catalogo:listar",
    "ejemplares:listar",
    "prestamos:listar",
    "reportes:listar",
])
def test_vistas_basicas_responden(client, admin, url_name):
    client.force_login(admin)
    resp = client.get(reverse(url_name))
    assert resp.status_code == 200
