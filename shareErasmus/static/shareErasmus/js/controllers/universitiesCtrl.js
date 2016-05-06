app.controller('UniversitiesCtrl', ['$scope', 'shareErasmusApi', function ($scope, shareErasmusApi){

    $scope.isCollapsed = true;
    $scope.withFilter = false;
    $scope.universities = [];
    $scope.selectedFilterObject = null;
    $scope.selectedFilterUniversity = null;
    $scope.cities = [];
    $scope.countries = [];
    $scope.countrySelected = null;
    $scope.citySelected = null;

    shareErasmusApi.getCities().then(function (response) {
        $scope.cities = response.data;
    });

    shareErasmusApi.getCountries().then(function (response) {
        $scope.countries = response.data;
    });

    shareErasmusApi.getUniversities().then(function (response) {
        $scope.universities = response.data;
    });

    $scope.$watch("selectedFilterObject",function(newValue,oldValue) {
        if (newValue != null) {
            $scope.selectedFilterUniversity = newValue.originalObject
            shareErasmusApi.getUniversity($scope.selectedFilterUniversity.pk).then(function (response) {
                $scope.universities = [];
                $scope.universities.push(response.data);
                $scope.withFilter = true;
            });
          return;
        }
      });

    $scope.restoreFilter = function() {
        $scope.withFilter = false;
        shareErasmusApi.getUniversities().then(function (response) {
            $scope.universities = response.data;
        });
    };

    $scope.changeSelectedCountry = function() {
        console.log($scope.countrySelected);
    };

    $scope.changeSelectedCity = function() {
        console.log($scope.citySelected);
        shareErasmusApi.getUniversityFilter($scope.citySelected).then(function (response) {
            $scope.universities = response.data;
            console.log(response.data);
            $scope.withFilter = true;
        });
    };


}]);