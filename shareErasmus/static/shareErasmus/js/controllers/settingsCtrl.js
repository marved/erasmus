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


    shareErasmusApi.getUniversities().then(function (response) {
        $scope.universities = response.data;
        $scope.countries = shareErasmusApi.loadCountries($scope.universities);

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
        $scope.filterCities = shareErasmusApi.loadCities($scope.universities, $scope.countrySelected);

    };

    var reloadFilterUniversities = function() {
        if ($scope.citySelected == null || $scope.citySelected == undefined) {
            $scope.filterUniversities = [];
            $scope.filterSubjects = [];
            return;
        }

        $scope.filterUniversities = [];
        for (var i=0; i<$scope.universities.length; i++) {
            if ($scope.universities[i].city == $scope.citySelected){
                $scope.filterUniversities.push($scope.universities[i]);
            }
        }
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
