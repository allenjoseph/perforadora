(function(){

    'use strict';

    var appServices = angular.module('appServices',['ngResource']);

    appServices.factory('MainService', ['$resource',
        function($resource){
            return $resource('modulos.json',{},{
                query : { method : 'GET', isArray:true }
            });
        }]);

    appServices.factory('MenuService',['$resource',
        function($resource){
            return $resource('modulos.json',{},{
                query : { method : 'GET', isArray:true }
            });
        }]);

    appServices.factory('PlanillaService', ['$resource',
        function($resource){
            return $resource('planilla/?format=json',{},{
                query : { method : 'GET' }
            });
        }]);

})();
