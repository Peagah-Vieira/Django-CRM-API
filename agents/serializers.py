from rest_framework import serializers
from .models import Agent


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'created_at',
            'updated_at',
        ]

    created_at = serializers.DateTimeField(
        format="%d/%b/%Y",
    )

    updated_at = serializers.DateTimeField(
        format="%d/%b/%Y",
    )
