from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import TodoItem
from .serializers import TodoItemSerializer
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.response import Response



class TodoItemViewSet(viewsets.ModelViewSet):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['patch'])
    def mark_completed(self, request, pk=None):
        todo_item = self.get_object()

        # Mark the Todo item as completed
        todo_item.completed = True
        todo_item.save()

        serializer = self.get_serializer(todo_item)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

def display_csrf_token(request):

    # get authorization token 
    token, created = Token.objects.get_or_create(user=request.user)


    return render(request, 'success_oauth.html', {'token':token.key})