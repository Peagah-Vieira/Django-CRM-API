from rest_framework.routers import SimpleRouter
from agents import views

app_name = "agents"

agents_api_route = SimpleRouter(trailing_slash=True)
agents_api_route.register(
    prefix='api',
    viewset=views.AgentAPIViewSet,
    basename='agents-api'
)

urlpatterns = agents_api_route.urls
