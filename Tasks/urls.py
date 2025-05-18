from django.urls import path
from .views import TaskListCreateView, TaskRetrieveUpdateDestroyView, UserRetrieveUpdateDestroyView, CreateUserView

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
    path('users/register/', CreateUserView.as_view(), name='user-register'),
    path('users/me/', UserRetrieveUpdateDestroyView.as_view(), name='current-user'),
]