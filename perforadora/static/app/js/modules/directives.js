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

    appDirectives.directive('appTable', function(){
        return{
            restrict : 'E',
            templateUrl : 'static/partials/table.tpl.html',
            scope : {
                data : '='
            }
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
