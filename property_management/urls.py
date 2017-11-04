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
from property_management.settings import shared
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework import routers
from clients.views import ClientViewSet
from real_estate.views import ComplexViewSet, BuildingViewSet, UnitViewSet
from users.views import TenantViewSet, AuthUserViewSet
from legal.views import LeaseViewSet
from billing.views import ChargeViewSet, PaymentViewSet
from communication.views import AnnouncementViewSet, MaintenanceRequestViewSet


router = routers.DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'properties', ComplexViewSet)
router.register(r'buildings', BuildingViewSet)
router.register(r'units', UnitViewSet)
router.register(r'users', AuthUserViewSet)
router.register(r'tenants', TenantViewSet)
router.register(r'leases', LeaseViewSet)
router.register(r'charges', ChargeViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'announcements', AnnouncementViewSet)
router.register(r'maintenance', MaintenanceRequestViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/auth/', include('users.urls', namespace='auth-api') ),
    url(r'^api/auth/get_token/', obtain_jwt_token),
    url(r'^api/', include(router.urls) ),
]

# Add these URLS in order for Django to be able to handle media files
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(
    shared.MEDIA_URL, document_root=shared.MEDIA_ROOT
)
