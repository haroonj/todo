from django.urls import path
from  .views import ListTodo,DetailTodo,getdata

urlpatterns =[
    path('',ListTodo.as_view()),
    path('<int:pk>/',DetailTodo.as_view()),
    path('one/<int:pk>/',getdata),
]