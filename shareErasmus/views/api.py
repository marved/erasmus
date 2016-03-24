from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework import viewsets, generics
from rest_framework import authentication, permissions

from django.contrib.auth.models import User
from shareErasmus.models import University, UserProfile, Subject, Comment
from shareErasmus.serializers import UniversitySerializer, UserProfileSerializer, SubjectSerializer, CommentSerializer


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


class UserProfileViewSet(CreateModelMixin,
                    RetrieveModelMixin,
                    DestroyModelMixin,
                    UpdateModelMixin,
                    ListModelMixin,
                    viewsets.GenericViewSet):
    """
    API endpoint that allows
    """
    queryset = UserProfile.objects.all().order_by('user')
    serializer_class = UserProfileSerializer


class SubjectViewSet(CreateModelMixin,
                    RetrieveModelMixin,
                    DestroyModelMixin,
                    UpdateModelMixin,
                    ListModelMixin,
                    viewsets.GenericViewSet):
    """
    API endpoint that allows
    """
    queryset = Subject.objects.all().order_by('name')
    serializer_class = SubjectSerializer


class CommentViewSet(CreateModelMixin,
                    RetrieveModelMixin,
                    DestroyModelMixin,
                    UpdateModelMixin,
                    ListModelMixin,
                    viewsets.GenericViewSet):
    """
    API endpoint that allows
    """
    queryset = Comment.objects.all().order_by('user')
    serializer_class = CommentSerializer
