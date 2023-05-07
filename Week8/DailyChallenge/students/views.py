from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
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

class StudentListView(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):
    def get_queryset(self):
        queryset = Student.objects.all().order_by('date_joined')
        return super().get_queryset()
    
    
    serializer_class = StudentSerializer


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
            return self.create(request, *args, **kwargs)

class StudentDetailView(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

