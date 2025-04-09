from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Task
from django.http import HttpResponse

from django.shortcuts import render
from .models import Task
from django.db.models import Count

def home(request):
    return HttpResponse("¡Bienvenido a la página principal!")


# Vista para listar las tareas
class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'


# Vista para ver los detalles de una tarea
class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'  # Esto hará que la tarea esté disponible en el contexto como 'task'


# Vista para crear nuevas tareas
class TaskCreateView(CreateView):
    model = Task
    template_name = 'tasks/task_form.html'
    fields = ['title', 'description', 'due_date', 'priority', 'status']
    success_url = reverse_lazy('tasks:list')
    
    def form_valid(self, form):
        # Aquí podrías agregar lógica adicional antes de guardar
        return super().form_valid(form)


# Vista para editar tareas existentes
class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'tasks/task_form.html'
    fields = ['title', 'description', 'due_date', 'priority', 'status']

    def get_success_url(self):
        # Redirige a la lista de tareas después de editar
        return reverse_lazy('tasks:list')


# Vista para eliminar tareas
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'

    def get_success_url(self):
        # Redirige a la lista de tareas después de eliminar
        return reverse_lazy('tasks:list')
    
def dashboard(request):
    # Contar tareas por estado
    task_status_counts = Task.objects.values('status').annotate(count=Count('status'))

    # Contar tareas por prioridad
    task_priority_counts = Task.objects.values('priority').annotate(count=Count('priority'))

    # Obtener todas las tareas con su fecha de vencimiento (para el calendario)
    task_due_dates = Task.objects.all()

    context = {
        'task_status_counts': task_status_counts,
        'task_priority_counts': task_priority_counts,
        'task_due_dates': task_due_dates,
    }

    return render(request, 'tasks/dashboard.html', context)