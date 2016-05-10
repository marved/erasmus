app.controller('UniversityDetailCtrl', ['$scope', 'shareErasmusApi', 'Notification', function ($scope, shareErasmusApi, Notification){

    var url = document.URL.split('/');
    $scope.universityId = url[url.length-1];
    $scope.university = null;

    shareErasmusApi.getUniversity($scope.universityId).then(function (response) {
        $scope.university = response.data;

        }, function (response) {
            console.log("Algo falló al buscar la universidad. Por favor, inténtelo más tarde");
    });

    shareErasmusApi.getLatLngGoogleMaps("Universidad Complutense de Madrid").then(function (response) {
        console.log(response.data);
        }, function (response) {
            console.log("Algo falló al buscar la universidad. Por favor, inténtelo más tarde");
        console.log(response.data);
    });

    $scope.map;
    $scope.service;
    $scope.infowindow;



    $scope.initialize = function() {

        var pyrmont = {lat: -3.8774878, lng: 40.3341186};

      map = new google.maps.Map(document.getElementById('university-detail-1-map'), {
          center: pyrmont,
          zoom: 15
        });

      var request = {
        location: pyrmont,
        radius: '50',
        query: 'urjc campus de fuenlabrada, fuenlabrada'
      };

      service = new google.maps.places.PlacesService(map);
      service.textSearch(request, callback);
        function callback(results, status) {
          if (status == google.maps.places.PlacesServiceStatus.OK) {
            for (var i = 0; i < results.length; i++) {
              var place = results[i];


            }
          }
        }
    };
    google.maps.event.addDomListener(window, "load", $scope.initialize());

}]);