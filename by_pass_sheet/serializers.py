from rest_framework import serializers
from .models import BypassSheet


class BypassSheetSerializer(serializers.ModelSerializer):
    bypass_sheet_field = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = BypassSheet
        # fields = '__all__'
        fields = ['id','title', 'text1', 'bypass_sheet_field' , 'text2','created_at' ]

