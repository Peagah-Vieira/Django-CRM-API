from rest_framework.viewsets import ModelViewSet
from .models import Agent
from .serializers import AgentSerializer


class AgentAPIViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
