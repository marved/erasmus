app.controller('SubjectDetailCtrl', ['$scope', 'shareErasmusApi', 'Notification', function ($scope, shareErasmusApi, Notification){

    var url = document.URL.split('/');
    $scope.subjectId = url[url.length-1];
    $scope.subject = null;
    $scope.users = [];
    $scope.students = [];

    shareErasmusApi.getSubject($scope.subjectId).then(function (response) {
        $scope.subject = response.data;
        shareErasmusApi.getUsers().then(function (response) {
            $scope.users = response.data;
            getStudentsInSubject();
            }, function (response) {
                console.log("Algo falló al buscar usuarios.");
        });
        }, function (response) {
            console.log("Algo falló al buscar la asignatura. Por favor, inténtelo más tarde");
    });

    var getStudentsInSubject = function() {
        for (var i=0; i<$scope.users.length; i++) {
            for (var j=0; j<$scope.users[i].subjects.length; j++) {
                if ($scope.users[i].subjects[j].pk == $scope.subject.pk)
                    $scope.students.push($scope.users[i]);
            }
        }
    };

}]);