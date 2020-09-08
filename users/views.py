from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from users.serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.http import require_http_methods
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
# Create your views here.
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
