from django.shortcuts import render
from  rest_framework import generics,status
from  rest_framework.response import Response  
from  rest_framework.decorators import api_view ,permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.contrib.auth import authenticate


from todos.models import Todo 
from account.models import Account
from .serializers import TodoSerializer,RegistrationSerializer




class ListTodo(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
#TODOS APIS
#TODOS LIST
@api_view(['GET',])
@permission_classes([IsAuthenticated])
def getTodosList(request):
    try:
        user = request.user
        todo_snipit = user.todo_set.all()
    except Todo.DoesNotExist :
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TodoSerializer(todo_snipit,many=True)
        return Response(serializer.data)


#CREATE TODO
@api_view(['POST',])
@permission_classes([IsAuthenticated])
def createTodo(request):

    user = request.user
    todo_snipit = Todo(author=user)

    if request.method == "POST":
        serializer = TodoSerializer(todo_snipit,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


#GET SINGLE TODO BY ID
@api_view(['GET',])
@permission_classes([IsAuthenticated])
def getTodo(request,pk):
    try:
	    todo_snipit = Todo.objects.get(id=pk)
    except Todo.DoesNotExist :
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TodoSerializer(todo_snipit)
        return Response(serializer.data)

#UPDATE TODO BY ID
@api_view(['PUT',])
@permission_classes([IsAuthenticated])
def upDateTodo(request,pk):
    try:
        todo_snipit = Todo.objects.get(id=pk)
    except Todo.DoesNotExist :
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    user = request.user
    if todo_snipit.author != user:
        return Response({'response':"you don't have the permission to edit this todo."})

    if request.method == "PUT":
        todo_snipit.author = request.user
        serializer = TodoSerializer(todo_snipit,data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            todo_snipit = Todo.objects.get(id=pk)
            serializer = TodoSerializer(todo_snipit)
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#DELETE TODO BY ID
@api_view(['DELETE',])
@permission_classes([IsAuthenticated])
def deleteTodo(request,pk):
    try:
        todo_snipit = Todo.objects.get(id=pk)
    except Todo.DoesNotExist :
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    user = request.user
    if todo_snipit.author != user:
        return Response({'response':"you don't have the permission to delete this todo."})
        
    if request.method == "DELETE":
        op = todo_snipit.delete()
        data = {}
        if op:
            data['success'] = 'deleted successfully'
            s =status.HTTP_204_NO_CONTENT
        else:
            data['failure'] = 'deletion failed'
            s = status.HTTP_400_BAD_REQUEST
        return Response(data=data,status=s)






#ACCOUNT APIS
#LOGIN
class ObtainAuthTokenView(APIView):

    authentication_classes = []
    permission_classes = []
    def post(self, request):
        context = {}

        email = request.POST.get('username')
        password = request.POST.get('password')
        account = authenticate(email=email, password=password)
        if account:
            try:
                token = Token.objects.get(user=account)
            except Token.DoesNotExist:
                token = Token.objects.create(user=account)
            context['response'] = 'Successfully authenticated.'
            context['pk'] = account.pk
            context['username'] = account.username         
            context['email'] = email.lower()
            context['token'] = token.key
            s=status.HTTP_200_OK
        else:
            s=status.HTTP_400_BAD_REQUEST
            context['response'] = 'Error'
            context['error_message'] = 'Invalid credentials'
        

        return Response(context,status=s)




#LOGOUT
@api_view(['POST',])
@permission_classes([IsAuthenticated])
def logOut(request, format=None):
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK,data={'response':'successfuly loged out'})




#REGISTER
@api_view(['POST',])
@permission_classes([])
def reg_user(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'successfully registered a new user.'
            data['email']    = account.email
            data['username']    = account.username
            token = Token.objects.get(user=account).key
            data['token']=token
            s=status.HTTP_200_OK
        else:
            s=status.HTTP_400_BAD_REQUEST
            data = serializer.errors
        
        return Response(data,status=s)