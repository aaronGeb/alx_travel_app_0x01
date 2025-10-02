from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from listings.views import ListingViewSet, BookingViewSet

router = routers.DefaultRouter()
router.register(r"listings", ListingViewSet)
router.register(r"bookings", BookingViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
