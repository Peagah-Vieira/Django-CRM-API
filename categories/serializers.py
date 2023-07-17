from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'description',
            'created_at',
            'updated_at',
        ]

    created_at = serializers.DateTimeField(
        format="%d/%b/%Y",
    )

    updated_at = serializers.DateTimeField(
        format="%d/%b/%Y",
    )
