
from django.urls import path,include
from . import views

urlpatterns = [
    path('add-task/',views.add_task,name='add_task'),

]