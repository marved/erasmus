app.controller('UniversitiesCtrl', ['$scope', function ($scope){

    $scope.isCollapsed = true;
    $scope.selectedFilterUniversity = null;

    $scope.universityFiltered = function() {
        if ($scope.selectedFilterUniversity != null)
            console.log($scope.selectedFilterUniversity);
    };

}]);