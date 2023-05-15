from django.shortcuts import render
from rest_framework import mixins, viewsets
from .permissions import IsSuperAdmin, IsManagementCompany, IsForMany
from .models import BypassSheet
from .serializers import BypassSheetSerializer
from .paginations import DocumentPagination


# Create your views here.
class BypassSheetViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = BypassSheet.objects.all()
    pagination_class = DocumentPagination
    serializer_class = BypassSheetSerializer
    # permission_classes = [IsForMany]