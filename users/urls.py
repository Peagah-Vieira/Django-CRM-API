from rest_framework.routers import SimpleRouter
from users import views

app_name = "users"

users_api_router = SimpleRouter(trailing_slash=True)
users_api_router.register(
    prefix='users/api',
    viewset=views.UserAPIViewSet,
    basename='users-api'
)

urlpatterns = users_api_router.urls
