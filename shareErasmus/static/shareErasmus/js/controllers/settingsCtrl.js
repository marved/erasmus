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

app.controller('SettingsCtrl', ['$scope', 'shareErasmusApi', function ($scope, shareErasmusApi){

    $scope.isCollapsed = true;
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


}]);
