from django.urls import path
from home import views


urlpatterns = [
    path('', views.todos_json, name='index_page'),
]