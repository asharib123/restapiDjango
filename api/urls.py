from django.urls import path
from . import views

urlpatterns = [
    path('', views.apioverview, name="api-overview"),
    path('task-list/', views.taskList, name="task-list"),
    path('task-detail/<str:pk>/', views.taskDetail, name="task-detail"),
    path('task-create/', views.taskCreate, name="task-create"),
    path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
    path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),


    path('', views.apioverview, name="api-overview"),
    path('employee-list/', views.employeeList, name="employee-list"),
    path('employee-detail/<str:pk>/',
         views.employeeDetail, name="employee-detail"),
    path('employee-create/', views.employeeCreate, name="employee-create"),
    path('employee-update/<str:pk>/',
         views.employeeUpdate, name="employee-update"),
    path('employee-delete/<str:pk>/',
         views.employeeDelete, name="employee-delete"),

]
