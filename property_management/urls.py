"""property_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view
from rest_framework import routers
from clients.views import ClientViewSet
from properties.views import BuildingViewSet, UnitViewSet
from tenants.views import TenantViewSet

schema_view = get_swagger_view(title='Property Management API')

router = routers.SimpleRouter()
router.register(r'clients', ClientViewSet, base_name='clients')
router.register(r'buildings', BuildingViewSet, base_name='buildings')
router.register(r'units', UnitViewSet, base_name='units')
router.register(r'tenants', TenantViewSet, base_name='tenants')

urlpatterns = [
    url(r'^$', schema_view),
    url(r'^admin/', admin.site.urls),
    url(r'^api/auth/', include('authentication.urls', namespace='auth-api') ),
    url(r'^api/', include(router.urls, namespace='api') ),
]
