app.controller('UniversitiesCtrl', ['$scope', 'shareErasmusApi', function ($scope, shareErasmusApi){

    $scope.isCollapsed = true;
    $scope.universities = [];
    $scope.selectedFilterObject = null;
    $scope.selectedFilterUniversity = null;
    $scope.$watch("selectedFilterObject",function(newValue,oldValue) {
        if (newValue != null) {
            $scope.selectedFilterUniversity = newValue.originalObject
            shareErasmusApi.getUniversityFilter($scope.selectedFilterUniversity.pk,
                                                $scope.selectedFilterUniversity.name).then(function (response) {
                $scope.universities = [];
                $scope.universities.push(response.data);
            });
          return;
        }
      });

    shareErasmusApi.getUniversities().then(function (response) {
        $scope.universities = response.data;
    });

    $scope.restoreFilter = function() {
        shareErasmusApi.getUniversities().then(function (response) {
            $scope.universities = response.data;
        });
    };


}]);