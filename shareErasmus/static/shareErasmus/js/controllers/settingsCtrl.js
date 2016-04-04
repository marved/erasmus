app.controller('SettingsCtrl', ['$scope', 'shareErasmusApi', function ($scope, shareErasmusApi){

    $scope.isCollapsed = true;
    $scope.universities = [];
    $scope.universitySelected = null;
    $scope.subjects = [];
    $scope.filterSubjects = [];
    $scope.subjectSelected = null;

    shareErasmusApi.getUniversities().then(function (response) {
        $scope.universities = response.data;
    });

    shareErasmusApi.getSubjects().then(function (response) {
        $scope.subjects = response.data;
    });


     var reloadFilterSubjects = function() {
        if ($scope.universitySelected == null || $scope.universitySelected == undefined) {
            console.log($scope.universitySelected);
            $scope.filterSubjects = $scope.subjects;
            return;
        }

        $scope.filterSubjects = [];
        for (var i=0; i<$scope.subjects.length; i++) {
            if ($scope.subjects[i].university == $scope.universitySelected){
                $scope.filterSubjects.push($scope.subjects[i]);
            }
        }
    };

    $scope.changeSelectedUniversity = function() {
        reloadFilterSubjects();
    };
}]);
