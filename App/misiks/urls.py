from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path, re_path
from rest_framework import routers
from api import views as api_views
from ui import views as ui_views

# API router
router = routers.DefaultRouter()
router.register(r'users', api_views.UserViewSet)
router.register(r'projects', api_views.ProjectViewSet)
router.register(r'roles', api_views.RoleViewSet)
router.register(r'specifications', api_views.SpecificationViewSet)
router.register(r'releases', api_views.ReleaseViewSet)
router.register(r'requirements', api_views.RequirementViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', ui_views.projects),
    path('releases/', ui_views.releases),
    re_path(r'(.*)logout/$', ui_views.logout_view),
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view()),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]