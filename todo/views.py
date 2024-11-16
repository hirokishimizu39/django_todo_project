from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import TodoModel
from django.urls import reverse_lazy

# Create your views here.
# ListViewを継承
class TodoList(ListView):
  template_name = 'list.html'
  model = TodoModel

# DetailViewを継承
class TodoDetail(DetailView):
  template_name = 'detail.html'
  model = TodoModel

# CreateViewを継承
class TodoCreate(CreateView):
  template_name = 'create.html'
  model = TodoModel
  fields = ('title', 'memo', 'priority', 'duedate')
  success_url = reverse_lazy('list')