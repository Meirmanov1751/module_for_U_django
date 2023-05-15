from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import BypassSheetViewSet

router = DefaultRouter()

router.register('bypassSheet/bypassSheet', BypassSheetViewSet)
