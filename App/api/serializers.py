from rest_framework import serializers
from api import models


class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Role
        fields = ['url', 'title', 'user', 'project']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    login = serializers.CharField(source='username')
    roles = RoleSerializer(many=True, required=False)
    
    class Meta:
        model = models.MisiksUser
        fields = ['url', 'login', 'first_name', 'patronymic_name', 'last_name', 'roles']


class RequirementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Requirement
        fields = ['url', 'name', 'project', 'type', 'description', 'create_date',\
        'modify_date', 'author', 'status', 'parent', 'release']


class RequirementWithChildrenSerializer(serializers.HyperlinkedModelSerializer):
    children = RequirementSerializer(many=True, required=False)
    
    class Meta:
        model = models.Requirement
        fields = ['url', 'name', 'project', 'type', 'description', 'create_date',\
        'modify_date', 'author', 'status', 'parent', 'release', 'children']


class ReleaseSerializer(serializers.HyperlinkedModelSerializer):
    requirements = RequirementWithChildrenSerializer(many=True, required=False)
    
    class Meta:
        model = models.Release
        fields = ['url', 'date', 'specification', 'approver', 'requirements']


class SpecificationSerializer(serializers.HyperlinkedModelSerializer):
    release = ReleaseSerializer(read_only=True, required=False)

    class Meta:
        model = models.Specification
        fields = ['url', 'name', 'create_date', 'modify_date', 'release']


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    users = RoleSerializer(many=True, required=False)
    requirements = RequirementWithChildrenSerializer(many=True, required=False)
    
    class Meta:
        model = models.Project
        fields = ['url', 'name', 'create_date', 'modify_date', 'author',\
        'description', 'state', 'users', 'requirements']