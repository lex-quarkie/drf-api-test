from rest_framework import serializers
from .models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    def get_queryset(self):
        return Application.objects.all()

    class Meta:
        model = Application
        fields = ["id", "name", "api_key"]
        read_only_fields = ["api_key"]
