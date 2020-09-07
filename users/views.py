from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from users.serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@csrf_exempt
def list_users(request):
    permission_classes = (IsAuthenticated,)
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, status=200, safe=False)

    return JsonResponse({'message':'Method Not Allowed'}, status=405)
