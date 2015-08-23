from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework import viewsets, generics
from rest_framework import authentication, permissions

from shareErasmus.models import University, Country
from shareErasmus.serializers import UniversitySerializer, CountrySerializer


class CountryViewSet(RetrieveModelMixin, ListModelMixin, viewsets.GenericViewSet):
    """
    API endpoint that allows
    """
    queryset = Country.objects.all().order_by('name')
    serializer_class = CountrySerializer

class UniversityViewSet(RetrieveModelMixin, ListModelMixin, viewsets.GenericViewSet):
    """
    API endpoint that allows
    """
    queryset = University.objects.all().order_by('name')
    serializer_class = UniversitySerializer
