'use strict';

define(['angular'],function(){

    var appDirectives = angular.module('appDirectives',[]);

    appDirectives.directive('appNav', function(){
        return {
            restrict : 'E',
            templateUrl : 'static/partials/nav.tpl.html',
            controller : 'MenuCtrl'
        };
    });

    appDirectives.directive('appDataTable', function(){
        return{
            restrict: 'E',
            templateUrl : 'static/partials/datatable.tpl.html'
        }
    });

    appDirectives.directive('appSideNav', function(){
        return{
            restrict: 'E',
            templateUrl : 'static/partials/sidenav.tpl.html'
        }
    })

    return appDirectives;

});
