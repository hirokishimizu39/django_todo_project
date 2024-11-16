from django.urls import path, include
from .views import TodoList, TodoDetail, TodoCreate, TodoDelete, TodoUpdate

urlpatterns = [
    path('list/', TodoList.as_view(), name='list'),
    # DetailViewは任意のデータを一つ取得して表示するという機能を持つため、primary_keyによって任意のデータを指定する
    path('detail/<int:pk>', TodoDetail.as_view(), name='detail'),
    path('create/', TodoCreate.as_view(), name='create'),
    # DeleteViewはどのデータを削除するのか一意に識別できる必要があるため、primary_keyによって任意のデータを指定する
    path('delete/<int:pk>', TodoDelete.as_view(), name='delete'),
    # UpdateViewはどのデータを更新するのか一意に識別できる必要があるため、primary_keyによって任意のデータを指定する
    path('update/<int:pk>', TodoUpdate.as_view(), name='update')
]
