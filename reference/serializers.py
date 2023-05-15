from rest_framework import serializers
from .models import Reference, ReferenceType


class ReferenceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferenceType
        fields = '__all__'


class ReferenceSerializer(serializers.ModelSerializer):
    # reference_type = ReferenceTypeSerializer()

    class Meta:
        model = Reference
        fields = '__all__'
        # fields = ['id','student', 'created_at', 'info', 'status', 'reference_type']
