from shareErasmus.models import University, UserProfile, Subject, Comment, Country, City
from rest_framework.serializers import ModelSerializer


class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = ('pk', 'name')


class CitySerializer(ModelSerializer):
    country = CountrySerializer
    class Meta:
        model = City
        fields = ('pk', 'name', 'country', 'description',
                  'prices', 'weather', 'student_life', 'culture',
                  'lodging', 'nightlife', 'information_interest')


class UniversitySerializer(ModelSerializer):
    city = CitySerializer
    class Meta:
        model = University
        fields = ('pk', 'name', 'city', 'description', 'validation_subjects', 'contacts')


class SubjectSerializer(ModelSerializer):
    university = UniversitySerializer
    class Meta:
        model = Subject
        fields = ('pk', 'name', 'difficulty', 'university')


class UserProfileSerializer(ModelSerializer):
    subjects = SubjectSerializer(many=True, required=False)
    class Meta():
        model = UserProfile
        fields = ('pk', 'username', 'first_name', 'last_name', 'email',
                  'last_login', 'date_joined', 'photo', 'password', 'is_public_email', 'subjects')

        read_only_fields = ('pk', 'date_joined')

    def create(self, validated_data):
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
        fields = ('pk', 'user', 'title', 'body', 'dateTime', 'university', 'subject', 'parent')

