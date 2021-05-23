from rest_framework import serializers
from api import models


class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Role
        fields = ['url', 'title', 'user', 'project']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    login = serializers.CharField(source='username')
    roles = RoleSerializer(many=True, required=False, read_only=True)
    
    class Meta:
        model = models.MisiksUser
        fields = ['url', 'login', 'first_name', 'patronymic_name', 'last_name', 'roles', 'password']


class RequirementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Requirement
        fields = ['url', 'name', 'project', 'type', 'description', 'create_date',\
        'modify_date', 'author', 'status', 'parent', 'specification', 'release']


class RequirementWithChildrenSerializer(serializers.HyperlinkedModelSerializer):
    children = RequirementSerializer(many=True, required=False, read_only=True)
    
    class Meta:
        model = models.Requirement
        fields = ['url', 'name', 'project', 'type', 'description', 'create_date',\
        'modify_date', 'author', 'status', 'parent', 'specification', 'release', 'children']


class SpecificationSerializer(serializers.HyperlinkedModelSerializer):
    requirements = RequirementWithChildrenSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = models.Specification
        fields = ['url', 'name', 'create_date', 'modify_date', 'description', 'requirements']


class ReleaseSerializer(serializers.HyperlinkedModelSerializer):
    specification = SpecificationSerializer()
    
    class Meta:
        model = models.Release
        fields = ['url', 'date', 'specification', 'approver']


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    users = RoleSerializer(many=True, required=False, read_only=True)
    requirements = RequirementWithChildrenSerializer(many=True, required=False, read_only=True)
    
    class Meta:
        model = models.Project
        fields = ['url', 'name', 'create_date', 'modify_date', 'author',\
        'description', 'state', 'users', 'requirements']