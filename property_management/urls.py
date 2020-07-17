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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)
from rest_framework import routers
from clients.views import ClientViewSet
from real_estate.views import ComplexViewSet, BuildingViewSet, UnitViewSet
from users.views import UserViewSet, obtain_token_admin, obtain_token_tenant
from legal.views import LeaseViewSet
from billing.views import ChargeViewSet, PaymentViewSet, InvoiceViewSet
from communication.views import AnnouncementViewSet, MaintenanceRequestViewSet


router = routers.DefaultRouter()
router.register(r"clients", ClientViewSet)
router.register(r"complexes", ComplexViewSet)
router.register(r"buildings", BuildingViewSet)
router.register(r"units", UnitViewSet)
router.register(r"users", UserViewSet)
router.register(r"leases", LeaseViewSet)
router.register(r"charges", ChargeViewSet)
router.register(r"payments", PaymentViewSet)
router.register(r"invoices", InvoiceViewSet)
router.register(r"announcements", AnnouncementViewSet)
router.register(r"maintenance", MaintenanceRequestViewSet)

app_name = "property_management"

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r"^api/", include(router.urls)),
    url(r"^api/auth/get_token/admin/", obtain_token_admin),
    url(r"^api/auth/get_token/tenant/", obtain_token_tenant),
    url(r"^api/auth/refresh_token/", TokenRefreshView.as_view()),
    url(r"^api/auth/verify_token/", TokenVerifyView.as_view()),
    url(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]

# Add these URLS in order for Django to be able to handle media files
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
