from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
# from users.views import list_users
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet
from users.views import UserCreateViewSet

retrieve_users = UserViewSet.as_view({
    'get': 'list'
})

create_user = UserCreateViewSet.as_view({
    'post': 'create'
})

urlpatterns = [
    path('users/', retrieve_users, name='retrieve-users'),
    path('users/register/', create_user, name='create-user'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
