app.controller('UserProfileCtrl', ['$scope', 'shareErasmusApi', function ($scope, shareErasmusApi){

    $scope.user = [];

    shareErasmusApi.getUser().then(function (response) {
        $scope.user = response.data;
    }, function (response) {

    });

}]);