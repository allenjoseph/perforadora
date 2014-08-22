(function(){

    'use strict';

    var app = angular.module('PerforadoraApp',['ngRoute', 'appControllers', 'appServices','appDirectives']);

    app.config(['$routeProvider',
        function($routeProvider){
            $routeProvider
            .when('/home',{
                templateUrl : 'static/partials/main.tpl.html',
                controller : 'MainCtrl'
            })
            .when('/planilla',{
                templateUrl : 'static/partials/planilla.tpl.html',
                controller : 'PlanillaListCtrl'
            })
            .otherwise({
                redirectTo : '/home'
            });
    }]);

})();
