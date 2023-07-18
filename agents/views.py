from rest_framework.viewsets import ModelViewSet
from .models import Agent
from .serializers import AgentSerializer


class AgentAPIViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

    def list(self, request, *args, **kwargs):
        """
            Return a list of all Agents from database.
        """
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
            Create a Agent on database.
        """
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
            Return a Agent from database.
        """
        return super().retrieve(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
            Applies partial update to a Agent.
        """
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
            Delete a Agent from database.
        """
        return super().destroy(request, *args, **kwargs)
