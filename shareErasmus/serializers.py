from shareErasmus.models import University, UserProfile, Subject, Comment
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer


class UniversitySerializer(ModelSerializer):
    class Meta:
        model = University
        fields = ('pk', 'name', 'country', 'city','description')


class UserSerializer(ModelSerializer):
    class Meta():
        model = User
        fields = ('pk', 'username', 'first_name', 'last_name', 'email', 'last_login', 'date_joined')


class UserProfileSerializer(ModelSerializer):
    user = UserSerializer()
    class Meta():
        model = UserProfile


class SubjectSerializer(ModelSerializer):
    university = UniversitySerializer
    users = UserProfileSerializer
    class Meta:
        model = Subject
        fields = ('pk', 'name', 'score', 'university', 'users')


class CommentSerializer(ModelSerializer):
    user = UserProfileSerializer
    university = UniversitySerializer
    subject = SubjectSerializer
    class Meta:
        model = Comment
        fields = ('pk', 'user', 'title', 'body', 'dateTime', 'university', 'subject')

