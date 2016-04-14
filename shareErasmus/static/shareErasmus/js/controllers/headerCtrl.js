app.controller('HeaderCtrl', ['$scope', 'shareErasmusApi', function ($scope, shareErasmusApi){

    $scope.user = {};
    $scope.isAuthenticated = false;

    shareErasmusApi.getSession().then(function (response) {
        $scope.user = response.data;
        $scope.isAuthenticated = true;
    }, function (response) {
        $scope.isAuthenticated = false;
    });

}]);