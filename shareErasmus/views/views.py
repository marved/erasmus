from django.shortcuts import render, redirect
from django.views.generic import View
from shareErasmus.models import University, Subject, UserProfile, City
from shareErasmus.views.maps import getLatLngData

class HomeView(View):
    def get(self, request):
        return render(request, "pages/index.html")


class SignView(View):
    def get(self, request):
        if request.user.is_authenticated():
            return redirect("/")
        else:
            return render(request, "pages/sign.html")


class UniversitiesView(View):
    def get(self, request):
        return render(request, "pages/universities.html")


class UniversityDetailView(View):
    def get(self, request, **kwargs):

        university_id = kwargs.get("id", None)
        if university_id:
            try:
                university = University.objects.get(pk=university_id)
            except:
                return render(request, "404.html")

            if university.latitude == None or university.longitude == None:
                latLng = getLatLngData(university.name, university.city.name)
                university.latitude = latLng['lat']
                university.longitude = latLng['lng']
                university.save()

            subjects = Subject.objects.all().filter(university=university_id).order_by('name')
            context = {
                'university': university,
                'subjects': subjects
            }
            return render(request, "pages/university-detail.html", context)

        else:
            return render(request, "404.html")


class SubjectDetailView(View):
    def get(self, request, **kwargs):

        subject_id = kwargs.get("id_subject", None)
        university_id = kwargs.get("id_university", None)
        if subject_id and university_id:
            try:
                subject = Subject.objects.get(pk=subject_id)
                if subject.university.pk == int(university_id):
                    context = {
                        'subject': subject
                    }
                    return render(request, "pages/subject-detail.html", context)
            except:
                pass

        return render(request, "404.html")


class UserProfileView(View):
    def get(self, request, **kwargs):
        username = kwargs.get("username", None)
        try:
            user = UserProfile.objects.get(username=username)
        except:
            return render(request, "404.html")

        subjects = user.subjects.all().order_by('name')
        universitiesName = []
        for subject in subjects:
            universitiesName.append(subject.university.name.encode("utf-8"))

        universitiesName = list(set(universitiesName))
        universities = []
        for universityName in universitiesName:
            try:
                universities.append(University.objects.get(name=universityName))
            except:
                pass

        context = {
                'user': user,
                'universities': universities,
                'subjects': subjects
            }
        return render(request, "pages/user-profile.html", context)


class ContactView(View):
    def get(self, request):
        return render(request, "pages/contact.html")

###############
#Settings views#
###############
class AccountView(View):
    def get(self, request):
        if request.user.is_authenticated():
            return render(request, "pages/settings/account.html")
        else:
            return render(request, "403.html")


class ChangePasswordView(View):
    def get(self, request):
        if request.user.is_authenticated():
            return render(request, "pages/settings/password.html")
        else:
            return render(request, "403.html")


class MyUniversitiesView(View):
    def get(self, request):
        if request.user.is_authenticated():
            user_id = request.user.pk
            try:
                user = UserProfile.objects.get(pk=user_id)
            except:
                return render(request, "403.html")
            subjects = user.subjects.all()
            universitiesName = []
            for subject in subjects:
                universitiesName.append(subject.university.name.encode("utf-8"))

            universitiesName = list(set(universitiesName))
            universities = []
            for universityName in universitiesName:
                try:
                    universities.append(University.objects.get(name=universityName))
                except:
                    pass
            context = {
                'universities': universities
            }
            return render(request, "pages/settings/my-universities.html", context)
        else:
            return render(request, "403.html")


class MySubjectsView(View):
    def get(self, request):
        if request.user.is_authenticated():
            user_id = request.user.pk
            user = UserProfile.objects.get(pk=user_id)
            subjects = user.subjects.all().order_by('name')
            universities = []
            for subject in subjects:
                universities.append(subject.university.name)

            universities = sorted(list(set(universities)))
            context = {
                'subjects': subjects,
                'universities': universities
            }
            return render(request, "pages/settings/my-subjects.html", context)
        else:
            return render(request, "403.html")


class MyCitiesView(View):
    def get(self, request):
        if request.user.is_authenticated():
            user_id = request.user.pk
            user = UserProfile.objects.get(pk=user_id)
            subjects = user.subjects.all()
            universitiesName = []
            for subject in subjects:
                universitiesName.append(subject.university.name)

            universitiesName = list(set(universitiesName))
            universities = []
            for universityName in universitiesName:
                try:
                    universities.append(University.objects.get(name=universityName))
                except:
                    pass

            cities = []
            for university in universities:
                cities.append(university.city)
            cities = sorted(list(set(cities)))
            context = {
                'cities': cities
            }
            return render(request, "pages/settings/my-cities.html", context)
        else:
            return render(request, "403.html")


class PrivacyPolicyView(View):
    def get(self, request):
        return render(request, 'privacy-policy.html')
