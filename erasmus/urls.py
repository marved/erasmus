"""erasmus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from shareErasmus.views.views import (
    HomeView, SignView, ContactView, UniversitiesView,
    AccountView, MyUniversitiesView, MySubjectsView,
    UniversityDetailView, SubjectDetailView)
from shareErasmus.views.api import (CountryViewSet, CityViewSet, UniversityViewSet, UserProfileViewSet,
                                    SubjectViewSet, CommentViewSet, SessionAPIView)
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'api/1.0/countries', CountryViewSet)
router.register(r'api/1.0/cities', CityViewSet)
router.register(r'api/1.0/universities', UniversityViewSet)
router.register(r'api/1.0/users', UserProfileViewSet)
router.register(r'api/1.0/subjects', SubjectViewSet)
router.register(r'api/1.0/comments', CommentViewSet)


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomeView.as_view()),
    url(r'^sign$', SignView.as_view()),
    url(r'^universities/(?P<id_university>[0-9]+)/(?P<id_subject>[0-9]+)$', SubjectDetailView.as_view()),
    url(r'^universities/(?P<id>[0-9]+)$', UniversityDetailView.as_view()),
    url(r'^universities$', UniversitiesView.as_view()),
    url(r'^contact$', ContactView.as_view()),
    url(r'^settings/account$', AccountView.as_view()),
    url(r'^settings/universities$', MyUniversitiesView.as_view()),
    url(r'^settings/subjects', MySubjectsView.as_view()),

    url(r'^logout$', 'shareErasmus.views.do_logout'),

    #API
    url(r'^', include(router.urls)),
    url(r'^api/1.0/session/$', SessionAPIView.as_view()),

    url(r'^.*$', 'shareErasmus.views.not_found'),
]
