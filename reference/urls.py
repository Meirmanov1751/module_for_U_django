from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ReferenceViewSet, ReferenceTypeViewSet

router = DefaultRouter()

router.register('reference/reference', ReferenceViewSet)
router.register('referenceType/referenceType', ReferenceTypeViewSet)
