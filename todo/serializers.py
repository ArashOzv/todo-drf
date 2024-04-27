from rest_framework import serializers
from todo.models import Todo
from django.contrib.auth import get_user_model
User = get_user_model()


class TodoSerializer(serializers.ModelSerializer):


    def validate_priority(self, priority):
        if priority < 10 or priority > 100:
            raise serializers.ValidationError("Priority must be between 10 and 100") 
        return priority
    
    class Meta:
        model = Todo
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    todos = TodoSerializer(read_only=True, many=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'todos']
        
