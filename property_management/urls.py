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
from entities.views import ClientViewSet
from properties.views import PropertyViewSet, BuildingViewSet, UnitViewSet
from tenants.views import TenantViewSet, OccupantTypeViewSet
from legal.views import LeaseViewSet

schema_view = get_swagger_view(title='Property Management API')

router = routers.SimpleRouter()
router.register(r'clients', ClientViewSet)
router.register(r'properties', PropertyViewSet)
router.register(r'buildings', BuildingViewSet)
router.register(r'units', UnitViewSet)
router.register(r'tenants', TenantViewSet)
router.register(r'occupant_type', OccupantTypeViewSet)
router.register(r'leases', LeaseViewSet)

urlpatterns = [
    url(r'^$', schema_view),
    url(r'^admin/', admin.site.urls),
    url(r'^api/auth/', include('authentication.urls', namespace='auth-api') ),
    url(r'^api/', include(router.urls) ),
]
