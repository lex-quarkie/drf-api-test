from uuid import uuid4

from .models import Application
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import ApplicationSerializer

from rest_framework import viewsets


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    @action(detail=True)
    def test(self, request):
        api_key = request.data.get("api_key")
        queryset = Application.objects.filter(api_key=api_key)
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)

    @action(detail=True)
    def change_key(self, request, pk):
        application = self.get_object()

        application.api_key = uuid4()
        application.save()

        serializer = self.serializer_class(application)
        return Response(serializer.data)
