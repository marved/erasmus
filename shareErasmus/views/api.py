#encoding:utf-8
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
    http_200_ok, http_201_created, http_400_bad_request, http_401_not_authorized,
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

    def create(self, request, *args, **kwargs):
        country_name = request.data.get("name", None);
        country, created = Country.objects.get_or_create(name=country_name)
        context = {"request": request}
        serializer = CountrySerializer(country, context=context)
        if created:
            return http_201_created(serializer.data)

        return http_200_ok(serializer.data)

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

    def create(self, request, *args, **kwargs):
        city_name = request.data.get("name", None);
        country = request.data.get("country", None);
        country_id = country.get("pk", None)
        try:
            country = Country.objects.get(pk=int(country_id))
        except:
            return http_400_bad_request(INVALID_CREDENTIALS_ERROR_MSG)
        city, created = City.objects.get_or_create(name=str(city_name), country=country)
        context = {"request": request}
        serializer = CitySerializer(city, context=context)
        if created:
            return http_201_created(serializer.data)
        return http_200_ok(serializer.data)

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

    def create(self, request, *args, **kwargs):
        university_name = request.data.get("name", None);
        city = request.data.get("city", None);
        city_id = city.get("pk", None);
        try:
            city = City.objects.get(pk=int(city_id))
        except:
            return http_400_bad_request(INVALID_CREDENTIALS_ERROR_MSG)
        university, created = University.objects.get_or_create(name=university_name, city=city)
        context = {"request": request}
        serializer = UniversitySerializer(university, context=context)
        if created:
            return http_201_created(serializer.data)
        return http_200_ok(serializer.data)


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

    def partial_update(self, request, *args, **kwargs):
        # Actualmente solo funciona en el caso de petición para añadir una asignatura al usuario
        subject = request.data.get("subject", None)
        user_id = kwargs.get("pk", None)
        #try:
        user = UserProfile.objects.get(pk=int(user_id))
        user.subjects.add(subject)
        user.save()
        return http_200_ok()

        #except:
         #   return http_400_bad_request(INVALID_CREDENTIALS_ERROR_MSG)


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
