from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework import viewsets, generics
from rest_framework import authentication, permissions

from django.contrib.auth import logout, login, authenticate
from django.contrib.sessions.models import Session
from shareErasmus.models import University, UserProfile, Subject, Comment, Country, City
from shareErasmus.serializers import (CountrySerializer, CitySerializer, UniversitySerializer,
                                      UserProfileSerializer, SubjectSerializer, CommentSerializer)

from shareErasmus.validators import LoginFormValidator
from shareErasmus.views.responses import (
    http_400_bad_request, http_401_not_authorized,
    INVALID_CREDENTIALS_ERROR_MSG, http_403_forbidden,
    USER_NOT_AUTHENTICATED_ERROR_MSG
)

class CountryViewSet(CreateModelMixin,
                    RetrieveModelMixin,
                    DestroyModelMixin,
                    UpdateModelMixin,
                    ListModelMixin,
                    viewsets.GenericViewSet):
    """
    API endpoint that allows
    """
    queryset = Country.objects.all().order_by('name')
    serializer_class = CountrySerializer


class CityViewSet(CreateModelMixin,
                    RetrieveModelMixin,
                    DestroyModelMixin,
                    UpdateModelMixin,
                    ListModelMixin,
                    viewsets.GenericViewSet):
    """
    API endpoint that allows
    """
    queryset = City.objects.all().order_by('name')
    serializer_class = CitySerializer

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
    queryset = UserProfile.objects.all().order_by('username')
    serializer_class = UserProfileSerializer

    def update(self, request, *args, **kwargs):
        user = request.user
        if not user.is_superuser:
            self.queryset = UserProfile.objects.filter(pk=user.pk)
        return super(UserProfileViewSet, self).update(request, *args, **kwargs)


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


class SessionAPIView(APIView):
    """
    Authentication methods.
    """
    queryset = Session.objects.none()  # Required for DjangoModelPermissions

    def get(self, request, format=None):
        user = request.user
        if user.is_authenticated():
            context = {"request": request}
            serializer = UserProfileSerializer(user, context=context)
            return Response(serializer.data)
        else:
            return http_403_forbidden(USER_NOT_AUTHENTICATED_ERROR_MSG)

    def post(self, request, format=None):
        form = LoginFormValidator(request.data)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is None:
                return http_401_not_authorized(INVALID_CREDENTIALS_ERROR_MSG)
            else:
                if user.is_active:
                    login(request, user)
                    context = {"request": request}
                    serializer = UserProfileSerializer(user, context=context)
                    return Response(serializer.data)
                else:
                    return http_401_not_authorized(INVALID_CREDENTIALS_ERROR_MSG)
        else:
            return http_400_bad_request(form.errors)

    def delete(self, request, format=None):
        logout(request)
        return Response()
