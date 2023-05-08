from django.shortcuts import render

from django.shortcuts import render
from .models import Department, Employee, Project,Task
from .serializers import *
from rest_framework import mixins,generics 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import (IsAdminUser,
                                        IsAuthenticated,
                                        AllowAny)
from rest_framework.status import (HTTP_200_OK,
                                   HTTP_201_CREATED,
                                   HTTP_204_NO_CONTENT,
                                   HTTP_400_BAD_REQUEST)
from .permissions import IsDepartmentAdmin

class DepartmentListAPIView(generics.ListAPIView):
    permission_classes = [IsDepartmentAdmin,]
    queryset = Department.objects.all().order_by('id')
    serializer_class = DepartmentSerializer

class DepartmentCreateAPIView(mixins.ListModelMixin ,generics.CreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
class DepartmentDetailAPIView(generics.RetrieveAPIView):
    permission_classes = (IsDepartmentAdmin, )
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentUpdateAPIView(mixins.DestroyModelMixin,mixins.RetrieveModelMixin,generics.UpdateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class EmployeeListAPIView(generics.ListAPIView):
    permission_classes = (IsDepartmentAdmin, )
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeCreateAPIView(mixins.ListModelMixin ,generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class EmployeeDetailAPIView(generics.RetrieveAPIView):
    permission_classes = (IsDepartmentAdmin, )
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeUpdateAPIView(mixins.RetrieveModelMixin,generics.UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
       return self.retrieve(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
       
class ProjectListAPIView(generics.ListAPIView):
    permission_classes = (IsDepartmentAdmin, )
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectCreateAPIView(mixins.ListModelMixin ,generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
class ProjectDetailAPIView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectUpdateAPIView(mixins.RetrieveModelMixin,mixins.DestroyModelMixin,generics.UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
       return self.retrieve(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class TaskListAPIView(generics.ListAPIView):
    permission_classes = (IsDepartmentAdmin, )
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskCreateAPIView(mixins.ListModelMixin ,generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class TaskDetailAPIView(generics.RetrieveAPIView):
    permission_classes = (IsDepartmentAdmin, )
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskUpdateAPIView(mixins.DestroyModelMixin,mixins.RetrieveModelMixin,generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
       return self.retrieve(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

