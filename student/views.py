from django.shortcuts import render
from rest_framework import mixins, viewsets
from .permissions import IsSuperAdmin, IsManagementCompany, IsForMany
from .models import Student
from .serializers import StudentSerializer
from .paginations import DocumentPagination


# Create your views here.
class StudentViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Student.objects.all()
    pagination_class = DocumentPagination
    serializer_class = StudentSerializer
    # permission_classes = [IsForMany]