from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from  .views import (
    ListTodo,
    DetailTodo,
    getTodosList,
    createTodo,
    getTodo,
    upDateTodo,
    deleteTodo,

    ObtainAuthTokenView,
    logOut,
    reg_user,
)

urlpatterns =[
    path('',ListTodo.as_view()),
    path('<int:pk>/',DetailTodo.as_view()),

    path('list/',getTodosList),
    path('create/',createTodo),
    path('get/<int:pk>/',getTodo),
    path('update/<int:pk>/',upDateTodo),
    path('delete/<int:pk>/',deleteTodo),

    path('register/',reg_user,name='register'),
    path('login/',ObtainAuthTokenView.as_view(),name='login'),
    path('logout/',logOut,name='logout'),

]