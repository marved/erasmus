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
    class Meta():
        model = UserProfile
        fields = ('pk', 'username', 'first_name', 'last_name', 'email', 'last_login', 'date_joined', 'photo', 'password')
        write_only_fields = ('password')
        read_only_fields = ('pk')

    def create(self, validated_data):
        user = UserProfile.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


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

