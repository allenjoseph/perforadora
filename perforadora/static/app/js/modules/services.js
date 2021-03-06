'use strict';

define(['angular','ngResource'], function(){

    var appServices = angular.module('appServices',['ngResource']);

    appServices.factory('MainService', ['$resource',function($resource){
        return $resource('modulos.json',{},{
            query : { method : 'GET', isArray:true }
        });
    }]);

    appServices.factory('MenuService',['$resource',function($resource){
        return $resource('modulos.json',{},{
            query : { method : 'GET', isArray:true }
        });
    }]);

    appServices.factory('PlanillaService', ['$resource',function($resource){
        return $resource('app/?format=json',{},{
            query : { method : 'GET' }
        });
    }]);

    appServices.factory('TrabajadorService', ['$resource',function($resource){
        return $resource('app/trabajador/?format=json',{},{
            query : { method : 'GET', isArray:true }
        });
    }]);

    appServices.factory('OcupacionService', ['$resource',function($resource){
        return $resource('app/ocupacion/?format=json',{},{
            query : { method : 'GET', isArray:true }
        });
    }]);

    appServices.factory('CategoriaService', ['$resource',function($resource){
        return $resource('app/categoria/?format=json',{},{
            query : { method : 'GET', isArray:true }
        });
    }]);
    return appServices;
});
