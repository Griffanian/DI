from rest_framework import serializers
from rest_framework.fields import empty
from .models import Department, Employee, Project,Task

class CustomHyperlinkedRelatedField(serializers.HyperlinkedRelatedField):
    def to_representation(self, value):
        default_repr = super().to_representation(value)
        dict_repr = {}
        if hasattr(value,'name'):
            dict_repr.update({'name':value.name})
        elif Department.objects.filter(id=value.pk).exists():
            dict_repr.update({'name':Department.objects.get(id=value.pk).name})
        dict_repr.update({'url':default_repr})
        return dict_repr

class ProjectSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(read_only=True,view_name='project-detail')
    tasks = CustomHyperlinkedRelatedField(many=True,read_only=True,view_name='task-detail')

    class Meta:
       model = Project
       fields = '__all__'

    def __init__(self, instance=None, data=..., **kwargs):
        super().__init__(instance, **kwargs)

        if self.context.get('hide_employees',True):
            self.fields.pop('employees')

class EmployeeSerializer(serializers.ModelSerializer):

    projects = CustomHyperlinkedRelatedField(many=True,read_only=True,view_name='project-detail')
    department = CustomHyperlinkedRelatedField(read_only=True,view_name='department-detail')
    url = serializers.HyperlinkedIdentityField(read_only=True,view_name='employee-detail')

    class Meta:
       model = Employee
       fields = '__all__'

    def get_fields(self):
        if self.context == {'hide':True}:
            self.fields.pop('department')
            self.fields.pop('projects')
        return super().get_fields()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['hide'] = False
        return context

    def get_projects(self, obj):
        projects = obj.projects.all()
        return ProjectSerializer(projects, many=True).data
    
    def get_url(self, obj, view_name, request, format):
        url = super().get_url(obj, view_name, request, format)
        context = {'hide':True}
        return url
    
class DepartmentSerializer(serializers.ModelSerializer):
    employees = CustomHyperlinkedRelatedField(many=True,read_only=True,view_name='employee-detail')
    url = serializers.HyperlinkedIdentityField(read_only=True,view_name='department-detail')

    class Meta:
       model = Department
       fields = '__all__'
       

class TaskSerializer(serializers.ModelSerializer):
    project = CustomHyperlinkedRelatedField(read_only=True,view_name='project-detail')
    url = serializers.HyperlinkedIdentityField(read_only=True,view_name='task-detail')
    
    class Meta:
       model = Task
       fields = '__all__'