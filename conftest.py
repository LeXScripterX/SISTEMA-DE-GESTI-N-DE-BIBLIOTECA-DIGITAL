# conftest.py  (raíz del repo)
import pytest
import datetime
import factory
from django.contrib.auth import get_user_model

User = get_user_model()

class AdminFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = "admin"
    email = "admin@test.com"
    first_name = "Ana"
    last_name = "Admin"
    password = factory.PostGenerationMethodCall("set_password", "Test1234")
    is_superuser = True
    is_staff = True
    tipo = "ADM"

@pytest.fixture
def admin(db):
    return AdminFactory()

@pytest.fixture
def recurso(db):
    # ⬇️  IMPORTA el modelo **aquí**, no arriba
    from catalogo.models import RecursoDigital
    return RecursoDigital.objects.create(
        titulo="Introducción a Python",
        autor="Guido van Rossum",
        tipo="LIB",
        descripcion="Libro de prueba",
        fecha_publicacion=datetime.date(2024, 1, 1),
        editorial="O'Reilly"
    )
