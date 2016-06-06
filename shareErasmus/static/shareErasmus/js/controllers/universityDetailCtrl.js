app.controller('UniversityDetailCtrl', ['$scope', 'shareErasmusApi', 'Notification', function ($scope, shareErasmusApi, Notification){

    var url = document.URL.split('/');
    $scope.universityId = url[url.length-1];
    $scope.university = null;

    shareErasmusApi.getUniversity($scope.universityId).then(function (response) {
        $scope.university = response.data;
        initMap();
        }, function (response) {
            console.log("Algo falló al buscar la universidad. Por favor, inténtelo más tarde");
    });

    var initMap = function() {

      // Create a map object and specify the DOM element for display.
      var map = new google.maps.Map(document.getElementById('university-detail-' + $scope.university.pk + '-map'), {
        center: {lat: $scope.university.latitude, lng: $scope.university.longitude},
        scrollwheel: true,
        zoom: 14
      });

      // Create a marker and set its position.
      var marker = new google.maps.Marker({
        map: map,
        position: {lat: $scope.university.latitude, lng: $scope.university.longitude},
        title: $scope.university.name
      });
    };

    $scope.WithInformation = function() {

    };

}]);