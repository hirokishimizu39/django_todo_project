from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import TodoModel

# Create your views here.
# ListViewを継承
class TodoList(ListView):
  template_name = 'list.html'
  model = TodoModel

# DetailViewを継承
class TodoDetail(DetailView):
  template_name = 'detail.html'
  model = TodoModel