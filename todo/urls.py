from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', views.TodosViewsetApiView)

urlpatterns = [
    # path('', views.all_todos, name='all_todos'),
    # path('<todo_id>', views.todo_detail_view, name='todo_detail_view'),
    # path('cbv/', views.TodosListApiVIew.as_view()),
    # path('cbv/<todo_id>', views.TodosDetailApiView.as_view()),
    # path('mixins/', views.TodosListMixinApiView.as_view()),\
    # path('mixins/<pk>', views.TodoDetailMixinApiView.as_view()),    
    # path('generics/', views.TodoGenericListApiView.as_view()),    
    # path('generics/<pk>', views.TodosGenericDetailView.as_view()),    
    path('viewsets/', include(router.urls)),
    path('users/', views.usersGenericListApiView.as_view()),
    
]