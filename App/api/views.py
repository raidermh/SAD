from rest_framework import viewsets
from rest_framework import permissions
from api import models, serializers


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.MisiksUser.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows projects to be viewed or edited.
    """
    queryset = models.Project.objects.all().order_by('-create_date')
    serializer_class = serializers.ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]


class RoleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows roles to be viewed or edited.
    """
    queryset = models.Role.objects.all().order_by('user')
    serializer_class = serializers.RoleSerializer
    permission_classes = [permissions.IsAuthenticated]


class SpecificationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows specifications to be viewed or edited.
    """
    queryset = models.Specification.objects.all().order_by('-create_date')
    serializer_class = serializers.SpecificationSerializer
    permission_classes = [permissions.IsAuthenticated]


class ReleaseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows releases to be viewed or edited.
    """
    queryset = models.Release.objects.all().order_by('-date')
    serializer_class = serializers.ReleaseSerializer
    permission_classes = [permissions.IsAuthenticated]


class RequirementViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows requirements to be viewed or edited.
    """
    queryset = models.Requirement.objects.all().order_by('-create_date')
    serializer_class = serializers.RequirementWithChildrenSerializer
    permission_classes = [permissions.IsAuthenticated]