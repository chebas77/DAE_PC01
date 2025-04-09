# DAE_PC01
# Dashboard de Productividad - Django & FullCalendar

Este es un proyecto de gestión de tareas que incluye un **dashboard** con gráficos, un calendario interactivo, y la posibilidad de visualizar el estado y la prioridad de las tareas. El proyecto está desarrollado con **Django**, **Chart.js** para los gráficos y **FullCalendar** para el calendario interactivo.

## Requisitos

Asegúrate de tener instalado lo siguiente antes de comenzar:

- **Python 3.x**: Este proyecto está desarrollado con Python 3.
- **Django**: Framework web utilizado para el backend.
- **Chart.js**: Librería para generar gráficos.
- **FullCalendar**: Librería para mostrar un calendario interactivo.

## Instrucciones para clonar y ejecutar el proyecto

### 1. Clona el repositorio

Primero, clona este repositorio en tu máquina local:

```bash
git clone https://github.com/tu_usuario/dashboard-productividad.git
2. Crea un entorno virtual (opcional pero recomendado)
Si deseas aislar las dependencias de este proyecto, crea un entorno virtual en Python:

bash
Copiar
Editar
cd dashboard-productividad
python -m venv venv
3. Activa el entorno virtual
En Windows:

bash
Copiar
Editar
venv\Scripts\activate
En macOS/Linux:

bash
Copiar
Editar
source venv/bin/activate
4. Instala las dependencias
Una vez activado el entorno virtual, instala las dependencias del proyecto:

bash
Copiar
Editar
pip install -r requirements.txt
5. Configura la base de datos
Si es la primera vez que estás configurando el proyecto, ejecuta las migraciones para crear la base de datos:

bash
Copiar
Editar
python manage.py migrate
6. Crea un superusuario (opcional)
Si deseas acceder al panel de administración de Django, crea un superusuario:

bash
Copiar
Editar
python manage.py createsuperuser
Sigue las instrucciones para establecer un nombre de usuario, correo electrónico y contraseña.

7. Ejecuta el servidor de desarrollo
Para iniciar el servidor de desarrollo de Django, ejecuta el siguiente comando:

bash
Copiar
Editar
python manage.py runserver
El servidor se ejecutará en http://127.0.0.1:8000/ y podrás acceder al sitio web desde tu navegador.

8. Accede al Dashboard
El dashboard se encuentra en http://127.0.0.1:8000/dashboard/, donde se muestra un gráfico de las tareas por estado y por prioridad, junto con un calendario interactivo.

El listado de tareas está disponible en http://127.0.0.1:8000/tasks/task-list/, donde podrás ver todas las tareas registradas.

Estructura del Proyecto
graphql
Copiar
Editar
dashboard-productividad/
├── manage.py               # Script para ejecutar el servidor y gestionar el proyecto Django
├── requirements.txt        # Lista de dependencias del proyecto
├── tasks/                  # Aplicación de tareas
│   ├── migrations/         # Migraciones de la base de datos
│   ├── __init__.py
│   ├── admin.py            # Configuración del panel de administración
│   ├── apps.py             # Configuración de la aplicación 'tasks'
│   ├── models.py           # Modelos de datos (definición de las tareas)
│   ├── views.py            # Vistas que generan las páginas de listado y dashboard
│   ├── urls.py             # Rutas de la aplicación de tareas
│   └── templates/
│       └── tasks/
│           ├── dashboard.html  # Plantilla del dashboard
│           └── task_list.html  # Plantilla del listado de tareas
├── config/                 # Configuración del proyecto Django
│   ├── __init__.py
│   ├── settings.py         # Configuración general del proyecto (base de datos, etc.)
│   ├── urls.py             # Rutas globales del proyecto
│   └── wsgi.py             # Configuración de WSGI para desplegar el proyecto
└── db.sqlite3              # Base de datos SQLite (se genera automáticamente)
Notas Adicionales
Este proyecto usa SQLite como base de datos, por lo que no es necesario configurar un servidor de base de datos externo.

Si deseas cambiar la base de datos (por ejemplo, usar PostgreSQL o MySQL), modifica las configuraciones de base de datos en el archivo config/settings.py.

Los gráficos se generan utilizando Chart.js, y el calendario interactivo usa FullCalendar.

Licencia
