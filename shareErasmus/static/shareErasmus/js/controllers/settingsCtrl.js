app.controller('SettingsCtrl', ['$scope', 'shareErasmusApi', function ($scope, shareErasmusApi){

    $scope.isCollapsed = true;
    $scope.universities = [];
    $scope.universitySelected = null;

    shareErasmusApi.getUniversities().then(function (response) {
        $scope.universities = response.data;
    });

}]);
