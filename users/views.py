from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer


class UserAPIViewSet(ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset
