from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.TaskListView.as_view(), name='list'),  # Definimos la URL para la lista de tareas
    path('create/', views.TaskCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', views.TaskUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.TaskDeleteView.as_view(), name='delete'),
]
