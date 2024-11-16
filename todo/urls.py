from django.urls import path, include
from .views import TodoList, TodoDetail

urlpatterns = [
    path('list/', TodoList.as_view()),
    # DetailViewは任意のデータを一つ取得して表示するため、primary_keyを指定
    path('detail/<int:pk>', TodoDetail.as_view())
]
