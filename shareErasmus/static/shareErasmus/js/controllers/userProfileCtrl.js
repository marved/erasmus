app.controller('UserProfileCtrl', ['$scope', 'shareErasmusApi', function ($scope, shareErasmusApi){

    $scope.universityIdSelected = null;

    $scope.changeUniversity = function(universityId) {
        $scope.universityIdSelected = universityId;
    };

    $scope.isActive = function(id) {
        return $scope.universityIdSelected == id;
    };
}]);