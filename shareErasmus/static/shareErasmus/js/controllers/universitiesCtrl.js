app.controller('UniversitiesCtrl', ['$scope', 'shareErasmusApi', function ($scope, shareErasmusApi){

    $scope.isCollapsed = true;
    $scope.withFilter = false;
    $scope.universities = [];
    $scope.universitiesMaps = [];
    $scope.selectedFilterObject = null;
    $scope.selectedFilterUniversity = null;
    $scope.cities = [];
    $scope.countries = [];
    $scope.countrySelected = null;
    $scope.citySelected = null;
    $scope.a = null;
    shareErasmusApi.getCities().then(function (response) {
        $scope.cities = response.data;
    });

    shareErasmusApi.getCountries().then(function (response) {
        $scope.countries = response.data;
    });

    shareErasmusApi.getUniversities().then(function (response) {
        $scope.universities = response.data;
        setTimeout(function(){$scope.initMap()}, 100);
    });

    $scope.$watch("selectedFilterObject",function(newValue,oldValue) {
        if (newValue != null) {
            $scope.selectedFilterUniversity = newValue.originalObject
            shareErasmusApi.getUniversity($scope.selectedFilterUniversity.pk).then(function (response) {
                $scope.universities = [];
                $scope.universities.push(response.data);
                $scope.withFilter = true;
                setTimeout(function(){$scope.initMap()}, 50);
            });
          return;
        }
      });

    $scope.restoreFilter = function() {
        $scope.withFilter = false;
        shareErasmusApi.getUniversities().then(function (response) {
            $scope.universities = response.data;
            setTimeout(function(){$scope.initMap()}, 50);
        });
    };

    $scope.changeSelectedCountry = function() {
        console.log($scope.countrySelected);
    };

    $scope.changeSelectedCity = function() {
        shareErasmusApi.getUniversityFilter($scope.citySelected).then(function (response) {
            $scope.universities = response.data;
            setTimeout(function(){$scope.initMap()}, 50);
            $scope.withFilter = true;
        });
    };

    $scope.initMap = function() {
        for (var i=0; i<$scope.universities.length; i++) {
            // Create a map object and specify the DOM element for display.
            var mapElement = document.getElementById("university-"+$scope.universities[i].pk+"-map");
            if( null === mapElement ) {
                console.log("ss");
                continue;
              }
            var map = new google.maps.Map(mapElement, {
            center: {lat: $scope.universities[i].latitude, lng: $scope.universities[i].longitude},
            scrollwheel: false,
            zoom: 14,
            mapTypeId: google.maps.MapTypeId.TERRAIN
            });
        }
    };


}]);