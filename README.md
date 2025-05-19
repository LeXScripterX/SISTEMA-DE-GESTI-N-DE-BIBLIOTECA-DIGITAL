
@@ -0,0 +1,53 @@


# 📚 Biblioteca Digital - Sistema de Gestión de Recursos Bibliográficos





Este proyecto es un sistema web de gestión de biblioteca digital desarrollado con Django. Permite autenticación de usuarios, búsqueda y filtrado de recursos, solicitudes de préstamo, reservas, renovaciones, notificaciones automáticas, y gestión completa de préstamos e inventario.





---





## 🚀 Características Principales





- Autenticación y permisos de usuarios


- Registro y consulta de usuarios


- Búsqueda básica y filtrado por categoría (libros, revistas, tesis)


- Visualización de detalles de los recursos


- Solicitudes de préstamo y reservas


- Renovaciones dentro del plazo permitido


- Notificaciones automáticas por vencimiento


- Generación de reportes


- Gestión de inventario y reglas del sistema





---





## 🛠️ Tecnologías Utilizadas





- **Python 3.12**


- **Django**


- **SQLite** (desarrollo), **PostgreSQL 14** (CI)


- **Pytest 8.3 + pytest-django 4.11**


- **FactoryBoy 3.3** para datos de prueba


- **GitHub Actions** para CI/CD


- **Google Sheets** como gestor de casos de prueba





---





## ⚙️ Instalación y Configuración





1. Clonar el repositorio:


   ```bash


   git clone https://github.com/LeXScripterX/SISTEMA-DE-GESTI-N-DE-BIBLIOTECA-DIGITAL.git


   cd SISTEMA-DE-GESTI-N-DE-BIBLIOTECA-DIGITAL


   ```


2. Crear y activar entorno virtual:





   ```bash


  python -m venv env


  source env/bin/activate  # Windows: env\Scripts\activate


  ```





3. Instalar dependencias:





   ```bash


   pip install -r requirements.txt


   ```