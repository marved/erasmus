app.controller('UniversityDetailCtrl', ['$scope', 'shareErasmusApi', 'Notification', function ($scope, shareErasmusApi, Notification){

    var url = document.URL.split('/');
    $scope.universityId = url[url.length-1];
    $scope.university = null;
    $scope.showAll = false;
    $scope.user = null;
    $scope.allComments = [];
    $scope.comments = [];
    $scope.isAuthenticated = false;

    shareErasmusApi.getUniversity($scope.universityId).then(function (response) {
        $scope.university = response.data;
        initMap();
        }, function (response) {
            console.log("Algo falló al buscar la universidad. Por favor, inténtelo más tarde");
    });

    shareErasmusApi.getSession().then(function (response) {
        getUser(response.data);
        $scope.isAuthenticated = true;
    }, function (response) {
        $scope.isAuthenticated = false;
        console.log("sin sesión iniciada.");
    });

    shareErasmusApi.getComments().then(function (response) {
        $scope.allComments = response.data;
        for (var i=0; i<$scope.allComments.length; i++) {
            if($scope.allComments[i].university != null)
                $scope.comments.push($scope.allComments[i]);
        }
    }, function (response) {
        console.log("Algo falló al cargar los comentarios.");
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

    $scope.withInformation = function(text) {
        return ((text != undefined) && (text!=""));
    };

    $scope.isShowedAllCategories = function() {
        $scope.showAll = !$scope.showAll;
    };

    var getUser = function(session) {
        shareErasmusApi.getUser(session.pk).then(function (response) {
            $scope.user = response.data;
        }, function (response) {
            console.log("Algo falló al buscar usuario.");
        });
    };

    $scope.saveComment = function() {
        shareErasmusApi.createComment($scope.user.pk, $scope.commentBody, $scope.university.pk, null).then(function (response) {
            Notification.success("Comentario añadido con éxito");
        }, function (response) {
            Notification.error("Error al añadir el comentario");
        });
    };

}]);