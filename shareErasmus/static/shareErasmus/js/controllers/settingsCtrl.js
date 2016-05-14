app.controller('AccountCtrl', ['$scope', 'shareErasmusApi', 'Notification', function ($scope, shareErasmusApi, Notification){

    $scope.user = {};
    $scope.checked = false;

    shareErasmusApi.getSession().then(function (response) {
        $scope.user = response.data;
        $scope.checked = $scope.user.is_public_email;
    });

    $scope.updateUserSend = function() {
        shareErasmusApi.updateUser($scope.user.pk,
                                    $scope.user.username,
                                    $scope.user.email,
                                    $scope.user.first_name,
                                    $scope.user.last_name,
                                    $scope.user.is_public_email,
                                    $scope.user.password)
            .then(function (response) {
                $scope.user =  response.data;
                Notification.success('Datos actualizados con éxito');
        }, function(response) {
            Notification.error("Algo falló al intentar actualizar la información de la cuenta. Por favor, inténtelo más tarde");
        });
    };
}]);

app.controller('MyUniversitiesCtrl', ['$scope', 'shareErasmusApi', 'Notification', function ($scope, shareErasmusApi, Notification){

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
                Notification.success("Asignaturas añadidas con éxito");
                $scope.subjectsSelected = [];
        }, function(response) {
            Notification.error("Algo falló al guardar las asignaturas seleccionadas. Por favor, inténtelo más tarde");
        });
    };

    var createSubjects = function(users) {
        shareErasmusApi.createSubjects($scope.subjectsCreatedName, $scope.universitySelected, $scope.user)
            .then(function (response) {
                Notification.success("Asignaturas creadas con éxito");
                $scope.subjectsCreatedName = [];
                if ($scope.subjectsSelected.length > 0)
                    addSubjectsSelectedToUser();
        }, function (response) {
            Notification.error("Algo falló al intentar crear asignaturas. Por favor, recargue la página e inténtelo más tarde");
        });
    };

    $scope.saveSubjects = function() {
        if ($scope.subjectsCreatedName.length > 0){
            createSubjects();
        }else {
            if ($scope.subjectsSelected.length > 0)
                    addSubjectsSelectedToUser();
        }
    };

}]);

app.controller('EditUniversityCtrl', ['$scope', 'shareErasmusApi', 'Notification', function ($scope, shareErasmusApi, Notification){

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
                Notification.success("Información de la universidad actualizada con éxito");
            }, function(response) {
                Notification.error("Algo falló al intentar actualizar información de la universidad. Por favor, inténtelo más tarde")
            });
    };

}]);

app.controller('CreateUniversityCtrl', ['$scope', 'shareErasmusApi', 'Notification', function ($scope, shareErasmusApi, Notification){

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
                Notification.success("Universidad creada con éxito");
                    $scope.countryName = [];
                    $scope.cityName = [];
                    $scope.universityName = [];
            }, function(response) {
                Notification.error("Algo falló al intentar crear una nueva universidad. Por favor, inténtelo más tarde");
            });
    };

    var createCity = function() {
        shareErasmusApi.createCity($scope.cityName, $scope.country)
            .then(function (response){
                $scope.city = response.data;
                createUniversity();
            }, function(response) {
                Notification.error("Algo falló al guardar la ciudad. Por favor, inténtelo más tarde");
            });
    };

    var createCountry = function() {
        shareErasmusApi.createCountry($scope.countryName)
            .then(function (response){
                $scope.country = response.data;
                createCity();
            }, function(response) {
                Notification.error("Algo falló al guardar el país. Por favor, inténtelo más tarde");
            });
    };

    $scope.saveUniversity = function() {
        createCountry();
    };

}]);

app.controller('EditSubjectCtrl', ['$scope', 'shareErasmusApi', 'Notification', function ($scope, shareErasmusApi, Notification){

    $scope.subject = null;
    $scope.difficulty = "";
    $scope.creditsEcts = "";
    $scope.getSubject = function(subjectId) {
        shareErasmusApi.getSubject(subjectId).then(function (response) {
            $scope.subject = response.data;
            $scope.difficulty = $scope.subject.difficulty_comment;
            $scope.creditsEcts = $scope.subject.credits_ects;
        });
    };

    $scope.updateSubject = function() {
        shareErasmusApi.updateInfoSubject($scope.subject.pk, $scope.difficulty, $scope.creditsEcts)
            .then(function (response){
                Notification.success("Información de la asignatura actualizada con éxito");
            }, function(response) {
                Notification.error("Algo falló al actualizar información de la asignatura. Por favor, inténtelo más tarde");
            });
    };

}]);

app.controller('EditCityCtrl', ['$scope', 'shareErasmusApi', 'Notification', function ($scope, shareErasmusApi, Notification){

    $scope.city = null;
    $scope.infoCity = {description: "", lodging: "", transport: "",
                        prices: "", mobilePhone: "", weather: "",
                        studentLife: "", nightlife: "", bankAccount: "",
                        restaurants: "", shopping: "", culture: "",
                        tourism: "", informationInterest: ""};
    $scope.getCity = function(cityId) {
        shareErasmusApi.getCity(cityId).then(function (response) {
            $scope.city = response.data;
            $scope.infoCity.description = $scope.city.description;
            $scope.infoCity.lodging = $scope.city.lodging;
            $scope.infoCity.transport = $scope.city.transport;
            $scope.infoCity.prices = $scope.city.prices;
            $scope.infoCity.mobilePhone = $scope.city.mobile_phone;
            $scope.infoCity.weather = $scope.city.weather;
            $scope.infoCity.studentLife = $scope.city.student_life;
            $scope.infoCity.nightlife = $scope.city.nightlife;
            $scope.infoCity.bankAccount = $scope.city.bank_account;
            $scope.infoCity.restaurants = $scope.city.restaurants;
            $scope.infoCity.shopping = $scope.city.shopping;
            $scope.infoCity.culture = $scope.city.culture;
            $scope.infoCity.tourism = $scope.city.tourism;
            $scope.infoCity.informationInterest = $scope.city.information_interest;
        });
    };

    $scope.updateCity = function() {
        shareErasmusApi.updateInfoCity($scope.city.pk, $scope.infoCity)
            .then(function (response){
                Notification.success("Información de la ciudad actualizada con éxito");
            }, function(response) {
                Notification.error("Algo falló al actualizar información de la ciudad. Por favor, inténtelo más tarde");
            });
    };

}]);
