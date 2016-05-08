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
        country_name = request.data.get("name", None)
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
        city_name = request.data.get("name", None)
        country = request.data.get("country", None)
        country_id = country.get("pk", None)
        try:
            country = Country.objects.get(pk=int(country_id))
        except:
            return http_400_bad_request(INVALID_CREDENTIALS_ERROR_MSG)
        city, created = City.objects.get_or_create(name=city_name.encode("utf-8"), country=country)
        context = {"request": request}
        serializer = CitySerializer(city, context=context)
        if created:
            return http_201_created(serializer.data)
        return http_200_ok(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        infoCity = request.data.get("infoCity", None)
        description = infoCity.get("description", None)
        lodging = infoCity.get("lodging", None)
        transport = infoCity.get("transport", None)
        prices = infoCity.get("prices", None)
        mobile_phone = infoCity.get("mobilePhone", None)
        weather = infoCity.get("weather", None)
        student_life = infoCity.get("studentLife", None)
        nightlife = infoCity.get("nightlife", None)
        bank_account = infoCity.get("bankAccount", None)
        restaurants = infoCity.get("restaurants", None)
        shopping = infoCity.get("shopping", None)
        culture = infoCity.get("culture", None)
        tourism = infoCity.get("tourism", None)
        information_interest = infoCity.get("informationInterest", None)
        city_id = kwargs.get("pk", None)
        try:
            city = City.objects.get(pk=int(city_id))
        except:
            return http_400_bad_request(INVALID_CREDENTIALS_ERROR_MSG)
        city.description = description.encode("utf-8")
        city.lodging = lodging.encode("utf-8")
        city.transport = transport.encode("utf-8")
        city.prices = prices.encode("utf-8")
        city.mobile_phone = mobile_phone.encode("utf-8")
        city.weather = weather.encode("utf-8")
        city.student_life = student_life.encode("utf-8")
        city.nightlife = nightlife.encode("utf-8")
        city.bank_account = bank_account.encode("utf-8")
        city.restaurants = restaurants.encode("utf-8")
        city.shopping = shopping.encode("utf-8")
        city.culture = culture.encode("utf-8")
        city.tourism = tourism.encode("utf-8")
        city.information_interest = information_interest.encode("utf-8")
        city.save()
        context = {"request": request}
        serializer = CitySerializer(city, context=context)
        return http_200_ok()

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
        university_name = request.data.get("name", None)
        city = request.data.get("city", None)
        city_id = city.get("pk", None)
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

    def partial_update(self, request, *args, **kwargs):
        description = request.data.get("description", None)
        validation_subjects = request.data.get("validationSubjects", None)
        contacts = request.data.get("contacts", None)
        university_id = kwargs.get("pk", None)
        try:
            university = University.objects.get(pk=int(university_id))
        except:
            return http_400_bad_request(INVALID_CREDENTIALS_ERROR_MSG)
        university.description = description.encode("utf-8")
        university.validation_subjects = validation_subjects.encode("utf-8")
        university.contacts = contacts.encode("utf-8")
        university.save()
        context = {"request": request}
        serializer = UniversitySerializer(university, context=context)
        return http_200_ok()

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = University.objects.all().order_by('name')
        name = self.request.query_params.get('name', None)
        city = self.request.query_params.get('city', None)
        if name is not None:
            queryset = queryset.filter(name__contains=name)
        if city is not None:
            queryset = queryset.filter(city=city)
        return queryset


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
        # Actualmente solo funciona este método en el caso de petición para añadir asignaturas al usuario
        subjects_id = request.data.get("subjects", None)
        user_id = kwargs.get("pk", None)
        #try:
        user = UserProfile.objects.get(pk=int(user_id))
        for subject_id in subjects_id:
            try:
                subject = Subject.objects.get(pk=subject_id)
            except:
                return http_400_bad_request(INVALID_CREDENTIALS_ERROR_MSG)
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

    def create(self, request, *args, **kwargs):
        subjects_name = request.data.get("names", None)
        university_id = request.data.get("university", None)
        user = request.data.get("user", None)
        user_id = user.get("pk", None)
        #try:
        user = UserProfile.objects.get(pk=user_id)
        for subject_name in subjects_name:
            try:
                university = University.objects.get(pk=int(university_id))
            except:
                return http_400_bad_request(INVALID_CREDENTIALS_ERROR_MSG)
            if subject_name != "" and subject_name != None:
                subject, created = Subject.objects.get_or_create(name=subject_name, university=university)
                user.subjects.add(subject)
        user.save()
        return http_201_created()

        #except:
         #   return http_400_bad_request(INVALID_CREDENTIALS_ERROR_MSG)

    def partial_update(self, request, *args, **kwargs):
        infoSubject = request.data.get("infoSubject", None)
        subject_id = kwargs.get("pk", None)
        try:
            subject = Subject.objects.get(pk=int(subject_id))
        except:
            return http_400_bad_request(INVALID_CREDENTIALS_ERROR_MSG)
        subject.difficulty_comment = infoSubject.encode("utf-8")
        subject.save()
        context = {"request": request}
        serializer = SubjectSerializer(subject, context=context)
        return http_200_ok()




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
