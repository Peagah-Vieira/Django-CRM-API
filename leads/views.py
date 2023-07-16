from rest_framework.viewsets import ModelViewSet
from .models import Lead
from .serializers import LeadSerializer


class LeadAPIViewSet(ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
