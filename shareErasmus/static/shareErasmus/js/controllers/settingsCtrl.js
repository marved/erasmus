app.controller('SettingsCtrl', ['$scope', 'shareErasmusApi', function ($scope, shareErasmusApi){

    $scope.isCollapsed = true;
    $scope.countries = [];
    $scope.countrySelected = null;
    $scope.universities = [];
    $scope.filterUniversities = [];
    $scope.universitySelected = null;
    $scope.subjects = [];
    $scope.filterSubjects = [];
    $scope.subjectsSelected = [];


    shareErasmusApi.getUniversities().then(function (response) {
        $scope.universities = response.data;
        loadCountries();
    });

    shareErasmusApi.getSubjects().then(function (response) {
        $scope.subjects = response.data;
    });

    var loadCountries = function() {
        for (var i=0; i<$scope.universities.length; i++) {
            if (!~$scope.countries.indexOf($scope.universities[i].country)) {
                $scope.countries.push($scope.universities[i].country);
            }
        }
    };

    var reloadFilterSubjects = function() {
        if ($scope.universitySelected == null || $scope.universitySelected == undefined) {
            console.log($scope.universitySelected);
            $scope.filterSubjects = $scope.subjects;
            return;
        }

        $scope.filterSubjects = [];
        for (var i=0; i<$scope.subjects.length; i++) {
            if ($scope.subjects[i].university == $scope.universitySelected){
                $scope.filterSubjects.push($scope.subjects[i]);
            }
        }
        console.log($scope.countrySelected);
    };

    var reloadFilterUniversities = function() {
        if ($scope.countrySelected == null || $scope.countrySelected == undefined) {
            $scope.filterUniversities = $scope.universities;
            return;
        }

        $scope.filterUniversities = [];
        for (var i=0; i<$scope.universities.length; i++) {
            if ($scope.universities[i].country == $scope.countrySelected){
                $scope.filterUniversities.push($scope.universities[i]);
            }
        }
    };

    $scope.changeSelectedUniversity = function() {
        reloadFilterSubjects();
    };

    $scope.changeSelectedCountry = function() {
        reloadFilterUniversities();
    };

}]);
