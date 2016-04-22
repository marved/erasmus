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
    $scope.subjectsCreated = [];


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
        }, function(response) {
            console.log("Algo falló en su solicitud. Por favor, inténtelo más tarde.");
        });
    };

    var createSubjects = function(users) {
        for (var i=0; i<$scope.subjectsCreated.length; i++) {
            if (!($scope.subjectsCreated[i] == undefined || $scope.subjectsCreated[i] == "")) {
                shareErasmusApi.createSubject($scope.subjectsCreated[i], $scope.universitySelected)
                    .then(function (response) {
                        console.log("Asignatura creada con éxito.");
                        shareErasmusApi.addSubjectsToUser($scope.user.pk, response.data.pk)
                            .then(function (response){
                                console.log("Asignatura añadida con éxito al usuario.");
                        }, function(response) {
                            console.log("Algo falló en su solicitud. Por favor, inténtelo más tarde.");
                        });

                }, function (response) {
                    console.log("Algo falló en su solicitud. Por favor, inténtelo más tarde.");
                });
            }
        }
    };

    $scope.saveSubjects = function() {
        createSubjects();
        $scope.subjectsCreated = [];
        addSubjectsSelectedToUser();
        $scope.subjectsSelected = [];
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
