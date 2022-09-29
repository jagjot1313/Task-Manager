from django.urls import path
from . import views

urlpatterns = [
    path('',views.openIndex),
    path('task-form',views.openTaskForm),
    path('tasks-list',views.getAllTasks),
    path('save-task',views.saveTask),
    path('mark-completed/<int:id>',views.markTaskAsCompleted),
    path('pending-tasks-list',views.getPendingTasks)
]