from rest_framework.routers import SimpleRouter
from leads import views

app_name = "leads"

leads_api_router = SimpleRouter(trailing_slash=True)
leads_api_router.register(
    prefix='api',
    viewset=views.LeadAPIViewSet,
    basename='leads-api'
)

urlpatterns = leads_api_router.urls
