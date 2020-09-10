from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profilepic.views import FileViewSet

router = DefaultRouter()
router.register('file', FileViewSet,basename='File')

urlpatterns = [
    path('',include(router.urls)),
]
