from rest_framework import serializers
from .models import Lead


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'category',
            'category_name',
            'agent',
            'agent_first_name',
            'created_at',
            'updated_at',
        ]

    category_name = serializers.StringRelatedField(
        source='category',
        read_only=True,
    )

    agent_first_name = serializers.StringRelatedField(
        source='agent',
        read_only=True,
    )

    created_at = serializers.DateTimeField(
        format="%d/%b/%Y",
    )

    updated_at = serializers.DateTimeField(
        format="%d/%b/%Y",
    )
