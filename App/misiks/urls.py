from ui.views import index
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from api import views
import ui

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'roles', views.RoleViewSet)
router.register(r'specifications', views.SpecificationViewSet)
router.register(r'releases', views.ReleaseViewSet)
router.register(r'requirements', views.RequirementViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', ui.views.index),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]