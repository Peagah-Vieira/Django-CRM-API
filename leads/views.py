from rest_framework.viewsets import ModelViewSet
from .models import Lead
from .serializers import LeadSerializer


class LeadAPIViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

    def list(self, request, *args, **kwargs):
        """
            Return a list of all Leads from database.
        """
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
            Create a Lead on database.
        """
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
            Return a Lead from database.
        """
        return super().retrieve(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
            Applies partial update to a Lead.
        """
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
            Delete a Lead from database.
        """
        return super().destroy(request, *args, **kwargs)
