from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework import viewsets, generics
from rest_framework import authentication, permissions

from shareErasmus.models import University
from shareErasmus.serializers import UniversitySerializer


class UniversityViewSet(CreateModelMixin,
                        RetrieveModelMixin,
                        DestroyModelMixin,
                        UpdateModelMixin,
                        ListModelMixin,
                        viewsets.GenericViewSet):
    """
    API endpoint that allows
    """
    queryset = University.objects.all().order_by('name')
    serializer_class = UniversitySerializer

