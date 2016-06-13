#encoding:utf-8
from shareErasmus.models import University, UserProfile, Subject, Comment, Country, City
from rest_framework.serializers import ModelSerializer, ValidationError


class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = ('pk', 'name')


class CitySerializer(ModelSerializer):
    country = CountrySerializer(required=True)
    class Meta:
        model = City
        fields = ('pk', 'name', 'country', 'description', 'lodging',
                  'transport', 'prices', 'mobile_phone', 'weather',
                  'student_life', 'nightlife', 'bank_account', 'restaurants',
                  'shopping', 'culture', 'tourism', 'information_interest')


class UniversitySerializer(ModelSerializer):
    city = CitySerializer(required=True)
    class Meta:
        model = University
        fields = ('pk', 'name', 'city', 'description', 'contacts', 'latitude', 'longitude')


class SubjectSerializer(ModelSerializer):
    university = UniversitySerializer(required=True)
    class Meta:
        model = Subject
        fields = ('pk', 'name', 'description', 'university', 'validation_subjects', 'credits_ects')


class UserProfileSerializer(ModelSerializer):
    subjects = SubjectSerializer(many=True, required=False)
    class Meta():
        model = UserProfile
        fields = ('pk', 'username', 'first_name', 'last_name', 'email',
                  'last_login', 'date_joined', 'photo', 'password', 'is_public_email', 'subjects')

        read_only_fields = ('pk', 'date_joined')

    def create(self, validated_data):
        user = UserProfile.objects.filter(email=validated_data['email'])
        if user:
            raise ValidationError("email")
        user = UserProfile.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class CommentSerializer(ModelSerializer):
    user = UserProfileSerializer
    university = UniversitySerializer
    subject = SubjectSerializer
    class Meta:
        model = Comment
        fields = ('pk', 'user', 'body', 'dateTime', 'university', 'subject', 'parent')

