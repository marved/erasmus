app.controller('SignUpCtrl', ['$scope', 'shareErasmusApi', 'Notification', function ($scope, shareErasmusApi, Notification){
    $scope.user = {"register_email": "", "register_username": "", "register_password": "", "register_repeat_password": ""};
    $scope.confirm_privacy_policy = false;

    $scope.createUserSend = function(){
        if (!$scope.confirm_privacy_policy) {
            Notification.warning("Debes aceptar la política de privacidad");
            $("#confirm-privacy-policy").focus();
            return;
        }
        shareErasmusApi.createUser($scope.user.register_email, $scope.user.register_username, $scope.user.register_password)
            .then(function (response) {
                $scope.user = {"register_email": "", "register_username": "", "register_password": "", "register_repeat_password": ""};
                Notification.success("Cuenta creada con éxito");
        }, function (response) {
                if (response.data.hasOwnProperty('email')) {
                    Notification.error("El correo electrónico ya existe");
                    $("#register-email").focus();
                } else if (response.data.hasOwnProperty('username')){
                    Notification.warning(response.data.username[0]);
                    $("#email-or-phone-number").focus();
                } else if (response.data.hasOwnProperty('password')){
                    Notification.warning(response.data.password[0]);
                    $("#register-password").focus();
                } else if (response.data[0] == "email"){
                    Notification.warning("El correo electrónico ya está registrado");
                } else {
                    console.log(response.data);
                    Notification.error("Algo falló al crear la cuenta. Por favor, inténtelo más tarde");

                }
        });
    };
}]);

app.controller('SignInCtrl', ['$scope', '$location', 'shareErasmusApi', 'Notification', function($scope, $location, shareErasmusApi, Notification) {
    $scope.user = {"username": "", "password": ""};

    $scope.signInSend = function(){
        shareErasmusApi.authenticate($scope.user.username, $scope.user.password)
            .then(function (response) {
                var next = shareErasmusApi.getUrlParameter('next');
                if (next == null || next == undefined || next == "") {
                    next = "/";
                }
                console.log(next);
                document.location.href = next;

        }, function (response) {
                if (response.data.hasOwnProperty('username')) {
                    console.log(response.data.username);
                    $("#login-username").focus();
                } else if (response.status == 401){
                    Notification.error("El usuario o contraseña introducidos no son correctos");
                    $("#login-username").focus();
                } else {
                    Notification.error("Algo falló al iniciar sesión. Por favor, inténtelo más tarde");
                }
        });
    };


}]);