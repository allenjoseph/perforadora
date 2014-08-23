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
            .when('/trabajador',{
                templateUrl : 'static/partials/trabajador.tpl.html',
                controller : 'TrabajadorListCtrl'
            })
            .otherwise({
                redirectTo : '/home'
            });
    }]);

})();
