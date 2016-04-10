app.controller('SignUpCtrl', ['$scope', 'shareErasmusApi', function ($scope, shareErasmusApi){
    $scope.user = {"register_email": "", "register_username": "", "register_password": ""};
    $scope.confirm_privacy_policy = false;

    $scope.createUserSend = function(){
        if (!$scope.confirm_privacy_policy) {
            console.log("Debes aceptar la política de privacidad.");
            $("#confirm-privacy-policy").focus();
            return;
        }
        shareErasmusApi.createUser($scope.user.register_email, $scope.user.register_username, $scope.user.register_password)
            .then(function (response) {
                $scope.user = {"register_email": "", "register_username": "", "register_password": ""};
        }, function (response) {
                console.log(response.data.register_email);
                if (response.data.hasOwnProperty('register_email')) {
                    console.log(response.data.register_email);
                    $("#register-email").focus();
                } else if (response.data.hasOwnProperty('register_username')){
                    console.log(response.data.username);
                    $("#email-or-phone-number").focus();
                } else if (response.data.hasOwnProperty('register_password')){
                    console.log(response.data.password);
                    $("#register-password").focus();
                } else {
                    console.log("Algo falló en su solicitud. Por favor, inténtelo más tarde.");
                }
        });
    };
}]);