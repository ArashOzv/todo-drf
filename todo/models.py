from django.db import models
from django.contrib.auth import get_user_model


user = get_user_model()


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField()
    priority = models.IntegerField(default=1)
    is_done = models.BooleanField(default=False)
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name='todos')
    def __str__(self):
        return f'{self.title} / is Done {self.is_done}'
    class Meta:
        db_table = 'todos'