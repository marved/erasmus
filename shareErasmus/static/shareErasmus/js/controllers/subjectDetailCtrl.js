app.controller('SubjectDetailCtrl', ['$scope', 'shareErasmusApi', 'Notification', function ($scope, shareErasmusApi, Notification){

    var url = document.URL.split('/');
    $scope.subjectId = url[url.length-1];
    $scope.subject = null;
    $scope.users = [];
    $scope.students = [];
    $scope.allComments = [];
    $scope.comments = [];
    $scope.user = null;
    $scope.isAuthenticated = false;
    $scope.commentBody = "";

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

    shareErasmusApi.getSession().then(function (response) {
        getUser(response.data);
        $scope.isAuthenticated = true;
    }, function (response) {
        $scope.isAuthenticated = false;
        console.log("Algo falló al buscar sesión.");
    });

    shareErasmusApi.getComments().then(function (response) {
        $scope.allComments = response.data;
        for (var i=0; i<$scope.allComments.length; i++) {
            if($scope.allComments[i].subject != null)
                $scope.allComments[i].dateTime = $scope.allComments[i].dateTime;
                $scope.comments.push($scope.allComments[i]);
        }
    }, function (response) {
        console.log("Algo falló al cargar los comentarios.");
    });

    var getStudentsInSubject = function() {
        for (var i=0; i<$scope.users.length; i++) {
            for (var j=0; j<$scope.users[i].subjects.length; j++) {
                if ($scope.users[i].subjects[j].pk == $scope.subject.pk)
                    $scope.students.push($scope.users[i]);
            }
        }
    };

    var getUser = function(session) {
        shareErasmusApi.getUser(session.pk).then(function (response) {
            $scope.user = response.data;
            console.log(($scope.user));
        }, function (response) {
            console.log("Algo falló al buscar usuario.");
        });
    };

    $scope.saveComment = function() {
        shareErasmusApi.createComment($scope.user.pk, $scope.commentBody, null, $scope.subject.pk).then(function (response) {
            Notification.success("Comentario añadido con éxito");
        }, function (response) {
            Notification.error("Error al añadir el comentario");
        });
    };

}]);