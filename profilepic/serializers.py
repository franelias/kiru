from rest_framework import serializers
from profilepic.models import File

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"

    def create(self, validated_data):
        file = File.objects.create(**validated_data)
        return file
