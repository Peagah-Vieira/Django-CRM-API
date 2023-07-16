from rest_framework.routers import SimpleRouter
from categories import views


app_name = "categories"

categories_api_route = SimpleRouter(trailing_slash=True)
categories_api_route.register(
    prefix='api',
    viewset=views.CategoryAPIViewSet,
    basename='categories-api'
)

urlpatterns = categories_api_route.urls
