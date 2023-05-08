"""
URL configuration for ExerciseXP project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from ManagmentAPI.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('departments/',DepartmentListAPIView.as_view(), name='department-list'),
    path('departments/create',DepartmentCreateAPIView.as_view(), name='department-create'),
    path('departments/<int:pk>',DepartmentDetailAPIView.as_view(), name='department-detail'),
    path('departments/<int:pk>/update/',DepartmentUpdateAPIView.as_view(), name='department-update'),

    path('employees/',EmployeeListAPIView.as_view(), name='employee-list'),
    path('employees/create',EmployeeCreateAPIView.as_view(), name='employee-create'),
    path('employees/<int:pk>',EmployeeDetailAPIView.as_view(), name='employee-detail'),
    path('employees/<int:pk>/update/',EmployeeUpdateAPIView.as_view(), name='employee-update'),

    path('projects/',ProjectListAPIView.as_view(), name='project-list'),
    path('projects/create',ProjectCreateAPIView.as_view(), name='project-create'),
    path('projects/<int:pk>',ProjectDetailAPIView.as_view(), name='project-detail'),
    path('projects/<int:pk>/update/',ProjectUpdateAPIView.as_view(), name='project-update'),

    path('tasks/',TaskListAPIView.as_view(), name='task-list'),
    path('tasks/create',ProjectCreateAPIView.as_view(), name='task-create'),
    path('tasks/<int:pk>',TaskDetailAPIView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/update/',TaskUpdateAPIView.as_view(), name='task-update'),

]
