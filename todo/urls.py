
from django.urls import path,include
from . import views

urlpatterns = [
    path('add-task/',views.add_task,name='add_task'),
    path("mark_as_done/<int:pk>/",views.mark_as_done,name='mark_as_done'),
    path("mark_as_undone/<int:pk>/",views.mark_as_undone,name='mark_as_undone'),
    path("edit-task/<int:pk>/",views.edit_task,name='edit_task'),
    path("delete-task/<int:pk>/",views.delete_task,name="delete_task")

]