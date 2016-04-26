app.controller('AccountCtrl', ['$scope', 'shareErasmusApi', function ($scope, shareErasmusApi){

    $scope.user = {};

    shareErasmusApi.getSession().then(function (response) {
        $scope.user = response.data;
    });

    $scope.updateUserSend = function() {
        shareErasmusApi.updateUser($scope.user.pk,
                                    $scope.user.username,
                                    $scope.user.email,
                                    $scope.user.first_name,
                                    $scope.user.last_name,
                                    $scope.user.password)
            .then(function (response) {
                $scope.user =  response.data;
                console.log("Datos actualizados con éxito.");
        });
    };
}]);

app.controller('MyUniversitiesCtrl', ['$scope', 'shareErasmusApi', function ($scope, shareErasmusApi){

    $scope.user = {};
    $scope.countries = [];
    $scope.countrySelected = null;
    $scope.cities = [];
    $scope.filterCities = [];
    $scope.citySelected = null;
    $scope.universities = [];
    $scope.filterUniversities = [];
    $scope.universitySelected = null;
    $scope.subjects = [];
    $scope.filterSubjects = [];
    $scope.subjectsSelected = [];
    $scope.subjectsCreatedName = [];


    shareErasmusApi.getSession().then(function (response) {
        $scope.user = response.data;
    });

    shareErasmusApi.getCountries().then(function (response) {
        $scope.countries = response.data;
    });

    shareErasmusApi.getCities().then(function (response) {
        $scope.cities = response.data;
    });

    shareErasmusApi.getUniversities().then(function (response) {
        $scope.universities = response.data;

    });

    shareErasmusApi.getSubjects().then(function (response) {
        $scope.subjects = response.data;
    });


    var reloadFilterCities = function() {
        if ($scope.countrySelected == null || $scope.countrySelected == undefined) {
            $scope.filterCities = [];
            $scope.filterUniversities = [];
            $scope.filterSubjects = [];
            return;
        }
        $scope.filterCities = shareErasmusApi.loadCities($scope.cities, $scope.countrySelected);

    };

    var reloadFilterUniversities = function() {
        if ($scope.citySelected == null || $scope.citySelected == undefined) {
            $scope.filterUniversities = [];
            $scope.filterSubjects = [];
            return;
        }
        $scope.filterUniversities = shareErasmusApi.loadUniversities($scope.universities, $scope.citySelected);
    };

    var reloadFilterSubjects = function() {
        if ($scope.universitySelected == null || $scope.universitySelected == undefined) {
            $scope.filterSubjects = [];
            return;
        }

        $scope.filterSubjects = [];
        for (var i=0; i<$scope.subjects.length; i++) {
            if ($scope.subjects[i].university == $scope.universitySelected){
                $scope.filterSubjects.push($scope.subjects[i]);
            }
        }
    };

    $scope.changeSelectedCountry = function() {
        reloadFilterCities();
    };

    $scope.changeSelectedCity = function() {
        reloadFilterUniversities();
    };

    $scope.changeSelectedUniversity = function() {
        reloadFilterSubjects();
    };

    var addSubjectsSelectedToUser = function() {
        shareErasmusApi.addSubjectsToUser($scope.user.pk, $scope.subjectsSelected)
            .then(function (response){
                console.log("Asignaturas añadidas con éxito al usuario.");
                $scope.subjectsSelected = [];
        }, function(response) {
            console.log("Algo falló en su solicitud. Por favor, inténtelo más tarde.");
        });
    };

    var createSubjects = function(users) {
        shareErasmusApi.createSubjects($scope.subjectsCreatedName, $scope.universitySelected, $scope.user)
            .then(function (response) {
                console.log("Asignaturas creadas con éxito.");
                $scope.subjectsCreatedName = [];
        }, function (response) {
            console.log("Algo falló en su solicitud. Por favor, inténtelo más tarde.");
        });
    };

    $scope.saveSubjects = function() {
        if ($scope.subjectsCreatedName.length > 0)
            createSubjects();
        if ($scope.subjectsSelected.length > 0)
            addSubjectsSelectedToUser();
    };

}]);

app.controller('EditUniversityCtrl', ['$scope', 'shareErasmusApi', function ($scope, shareErasmusApi){

    $scope.university = null;
    $scope.description = "";
    $scope.validationSubjects = "";
    $scope.contacts = "";

    $scope.getUniversity = function(universityId) {
        shareErasmusApi.getUniversity(universityId).then(function (response) {
            $scope.university = response.data;
            $scope.description = $scope.university.description;
            $scope.validationSubjects = $scope.university.validation_subjects;
            $scope.contacts = $scope.university.contacts;
        });
    };

    $scope.updateUniversity = function() {
        shareErasmusApi.updateInfoUniversity($scope.university.pk,
                                            $scope.description,
                                            $scope.validationSubjects,
                                            $scope.contacts)
            .then(function (response){
                console.log("Información de la universidad actualizada con éxito.");
            }, function(response) {
                console.log("Algo falló en su solicitud. Por favor, inténtelo más tarde.");
            });
    };

}]);

app.controller('CreateUniversityCtrl', ['$scope', 'shareErasmusApi', function ($scope, shareErasmusApi){

    $scope.countryName = [];
    $scope.country = [];
    $scope.cityName = [];
    $scope.city = [];
    $scope.universityName = [];

    shareErasmusApi.getCountries().then(function (response) {
        $scope.countries = response.data;
    });

    shareErasmusApi.getCities().then(function (response) {
        $scope.cities = response.data;
    });

    shareErasmusApi.getUniversities().then(function (response) {
        $scope.universities = response.data;

    });

    var createUniversity = function() {
        shareErasmusApi.createUniversity($scope.universityName, $scope.city)
            .then(function (response){
                console.log("Universidad creada con éxito.");
                    $scope.countryName = [];
                    $scope.cityName = [];
                    $scope.universityName = [];
            }, function(response) {
                console.log("Algo falló en su solicitud. Por favor, inténtelo más tarde.");
            });
    };

    var createCity = function() {
        shareErasmusApi.createCity($scope.cityName, $scope.country)
            .then(function (response){
                $scope.city = response.data;
                createUniversity();
                console.log("Ciudad creada con éxito.");
            }, function(response) {
                console.log("Algo falló en su solicitud. Por favor, inténtelo más tarde.");
            });
    };

    var createCountry = function() {
        shareErasmusApi.createCountry($scope.countryName)
            .then(function (response){
                $scope.country = response.data;
                createCity();
                console.log("País creado con éxito.");
            }, function(response) {
                console.log("Algo falló en su solicitud. Por favor, inténtelo más tarde.");
            });
    };

    $scope.saveUniversity = function() {
        createCountry();
    };

}]);

app.controller('EditSubjectCtrl', ['$scope', 'shareErasmusApi', function ($scope, shareErasmusApi){

    $scope.subject = null;
    $scope.infoSubject = "";
    $scope.getSubject = function(subjectId) {
        shareErasmusApi.getSubject(subjectId).then(function (response) {
            $scope.subject = response.data;
            $scope.infoSubject = $scope.subject.difficulty_comment;
        });
    };

    $scope.updateSubject = function() {
        shareErasmusApi.updateInfoSubject($scope.subject.pk, $scope.infoSubject)
            .then(function (response){
                console.log("Información de la asignatura actualizada con éxito.");
            }, function(response) {
                console.log("Algo falló en su solicitud. Por favor, inténtelo más tarde.");
            });
    };

}]);

app.controller('EditCityCtrl', ['$scope', 'shareErasmusApi', function ($scope, shareErasmusApi){

    $scope.city = null;
    $scope.infoCity = {description: "", lodging: "", prices: "",
                        weather: "", studentLife: "", culture: "",
                        nightlife: "", informationInterest: ""};
    $scope.getCity = function(cityId) {
        shareErasmusApi.getCity(cityId).then(function (response) {
            $scope.city = response.data;
            $scope.infoCity.description = $scope.city.description;
            $scope.infoCity.lodging = $scope.city.lodging;
            $scope.infoCity.prices = $scope.city.prices;
            $scope.infoCity.weather = $scope.city.weather;
            $scope.infoCity.studentLife = $scope.city.student_life;
            $scope.infoCity.culture = $scope.city.culture;
            $scope.infoCity.nightlife = $scope.city.nightlife;
            $scope.infoCity.informationInterest = $scope.city.information_interest;
        });
    };

    $scope.updateCity = function() {
        shareErasmusApi.updateInfoCity($scope.city.pk, $scope.infoCity)
            .then(function (response){
                console.log("Información de la ciudad actualizada con éxito.");
            }, function(response) {
                console.log("Algo falló en su solicitud. Por favor, inténtelo más tarde.");
            });
    };

}]);
