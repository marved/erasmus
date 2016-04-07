app.service('shareErasmusApi', ['$http',  function($http) {

    var UNIVERSITIES_PATH = "/api/1.0/universities";
    var SUBJECTS_PATH = "/api/1.0/subjects";
    var USERS_PATH = "/api/1.0/users";
    var COMMENTS_PATH = "/api/1.0/comments";

    var X_CSRF_TOKEN_HEADER_NAME = "X-CSRFToken";
    var COOKIE_HEADER_NAME = "Cookie";

    var config = {
        headers:  {
            'Accept-Language': 'es',
            'Content-Type': 'application/json'
        }
    };

    var urlEncode = function(obj) {
        var str = [];
        for(var p in obj)
            if (obj.hasOwnProperty(p)) {
              str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]));
            }
        return str.join("&");
    };

    var defaultHeaders = function() {
        var xHeaders = config.headers;
        return xHeaders;
    };

    var _http = function(method, url, query_params, data, headers, transformRequest) {
        query_params = query_params || null;
        data = data || null;
        headers = headers || defaultHeaders();
        transformRequest = transformRequest || null;

        if (transformRequest != null)
            var req = {
                method: method,
                url: url,
                headers: headers,
                params: query_params,
                data: data,
                transformRequest: transformRequest
            };
        else
            var req = {
                method: method,
                url: url,
                headers: headers,
                params: query_params,
                data: data
            };

        return $http(req);
    };

    this.getUniversities = function() {
        return _http("GET", UNIVERSITIES_PATH);
    };

    this.getSubjects = function() {
        return _http("GET", SUBJECTS_PATH);
    };

    this.getUsers = function() {
        return _http("GET", USERS_PATH);
    };

    this.getComments = function() {
        return _http("GET", COMMENTS_PATH);
    };

    this.loadCountries = function(universities) {
        var countries = [];
        for (var i=0; i<universities.length; i++) {
            if (!~countries.indexOf(universities[i].country)) {
                countries.push(universities[i].country);
            }
        }
        return countries;
    };

    this.loadCities = function(universities, country) {
        var cities = [];
        for (var i=0; i<universities.length; i++) {
            if (!~cities.indexOf(universities[i].city) && universities[i].country == country) {
                cities.push(universities[i].city);
            }
        }
        return cities;
    };





    this.getCountries = function() {

    };


}]);