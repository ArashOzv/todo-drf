from django.http import JsonResponse
from django.shortcuts import render
from todo.models import Todo
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.
def index(request):
    todos = Todo.objects.order_by('priority').all()
    context = {
        'todos' : todos
    }
    return render(request, 'home/index.html', context)


@api_view(['GET'])
def todos_json(request: Request):
    todos = list(Todo.objects.order_by('priority').all().values('title', 'is_done'))

    return Response({'todos':todos}, status.HTTP_200_OK)
    