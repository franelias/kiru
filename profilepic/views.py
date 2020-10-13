from rest_framework.parsers import FileUploadParser
from rest_framework import viewsets
from profilepic.serializers import FileSerializer
from rest_framework.permissions import IsAuthenticated
from profilepic.models import File

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = (IsAuthenticated,)
    parser_class = (FileUploadParser,)
