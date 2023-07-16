from rest_framework.viewsets import ModelViewSet
from .models import Lead
from .serializers import LeadSerializer


class LeadAPIViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
