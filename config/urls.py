from django.contrib import admin
from django.urls import path, include
from tasks import views  # Importa la vista para el dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),  # Las rutas de tareas van aquí
    path('dashboard/', views.dashboard, name='dashboard'),  # Ruta independiente para el dashboard
]
