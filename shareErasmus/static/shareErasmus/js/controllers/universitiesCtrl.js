app.controller('UniversitiesCtrl', ['$scope', 'shareErasmusApi', function ($scope, shareErasmusApi){

    $scope.isCollapsed = true;
    $scope.universities = []
    $scope.selectedFilterUniversity = null;

    shareErasmusApi.getUniversities().then(function (response) {
        $scope.universities = response.data;
    });

    $scope.universityFiltered = function() {
        if ($scope.selectedFilterUniversity != null)
            console.log($scope.selectedFilterUniversity);
    };

}]);