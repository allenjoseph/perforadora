'use strict';

define(['angular'],function(){

    var appDirectives = angular.module('appDirectives',[]);

    appDirectives.directive('appMenu', function(){
        return {
            restrict : 'E',
            templateUrl : 'static/partials/nav.tpl.html'
        };
    });

    appDirectives.directive('appDataTable', function(){
        return{
            restrict: 'E',
            templateUrl : 'static/partials/datatable.tpl.html'
        }
    });

    return appDirectives;

});
