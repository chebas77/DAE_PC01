from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task

from django.http import HttpResponse

def home(request):
    return HttpResponse("¡Bienvenido a la página principal!")


# Vista para listar las tareas
class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

# Vista para crear nuevas tareas
class TaskCreateView(CreateView):
    model = Task
    template_name = 'tasks/task_form.html'
    fields = ['title', 'description', 'due_date', 'priority', 'status']
    
    def form_valid(self, form):
        # Aquí podrías agregar lógica adicional antes de guardar
        return super().form_valid(form)

# Vista para editar tareas existentes
class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'tasks/task_form.html'
    fields = ['title', 'description', 'due_date', 'priority', 'status']

# Vista para eliminar tareas
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task_list')
