from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),  # Incluye las rutas de la app 'tasks'
    path('', RedirectView.as_view(url='/tasks/', permanent=True)),  # Redirige la raíz a 'tasks/'
]
