from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
# from users.views import list_users
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
