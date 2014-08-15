(function(){

    'use strict';

    var appServices = angular.module('appServices',['ngResource']);

    appServices.factory('MainService', ['$resource',
        function($resource){
            return $resource('modulos.json',{},{
                query : { method : 'GET', isArray:true }
            });
    }]);

    appServices.factory('Planilla', ['$resource',
        function($resource){
            return $resource('planilla/?format=json',{},{
                query : { method : 'GET' }
            });
    }]);

})();
