from django.urls import path, include
from .views import TodoList, TodoDetail, TodoCreate

urlpatterns = [
    path('list/', TodoList.as_view(), name='list'),
    # DetailViewは任意のデータを一つ取得して表示するという機能を持つため、primary_keyによって任意のデータを指定する
    path('detail/<int:pk>', TodoDetail.as_view(), name='detail'),
    path('create/', TodoCreate.as_view(), name='create')
]
