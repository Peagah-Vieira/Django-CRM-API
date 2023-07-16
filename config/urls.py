from django.contrib import admin
from django.urls import include, path
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path(
        'api_schema/',
        get_schema_view(
            title='Django-CRM-API Schema',
            description='Guide for the Django-CRM-API'
        ),
        name='api_schema'
    ),
    path(
        '',
        TemplateView.as_view(
            template_name='swagger-ui.html',
            extra_context={'schema_url': 'api_schema'}
        ),
        name='swagger_ui',
    ),
    path(
        'api/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'api/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path(
        'api/token/verify/',
        TokenVerifyView.as_view(),
        name='token_verify'
    ),
    path(
        'accounts/',
        include('accounts.urls'),
    ),
    path(
        'categories/',
        include('categories.urls'),
    ),
    path(
        'agents/',
        include('agents.urls'),
    ),
    path(
        'leads/',
        include('leads.urls'),
    ),
    path(
        'admin/',
        admin.site.urls,
    ),
]
