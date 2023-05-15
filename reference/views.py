from django.shortcuts import render
from rest_framework import mixins, viewsets
from .permissions import IsSuperAdmin, IsManagementCompany, IsForMany
from .models import Reference, ReferenceType
from .serializers import ReferenceSerializer, ReferenceTypeSerializer
from .paginations import DocumentPagination


# Create your views here.
class ReferenceViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Reference.objects.all()
    pagination_class = DocumentPagination
    serializer_class = ReferenceSerializer
    # permission_classes = [IsForMany]

class ReferenceTypeViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = ReferenceType.objects.all()
    pagination_class = DocumentPagination
    serializer_class = ReferenceTypeSerializer