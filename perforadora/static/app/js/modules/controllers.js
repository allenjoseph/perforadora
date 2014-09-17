'use strict';

define(['angular'],function(){

    var appControllers = angular.module('appControllers',[]);

    appControllers.controller('MainCtrl',['$scope', 'MainService',
    function($scope, MainService){
        $scope.modulos = MainService.query();
    }]);

    appControllers.controller('PlanillaListCtrl',['$scope', 'PlanillaService',
    function($scope, PlanillaService){
        $scope.planilla = PlanillaService.query();
    }]);

    appControllers.controller('MenuCtrl', ['$scope', 'MenuService',
    function($scope, MenuService){
        var ng = $scope;

        ng.modulos = MenuService.query();

        ng.menuActive = 'home';

        ng.selectMenu = function(menu){

            ng.menuActive = menu;
        }
    }]);

    appControllers.controller('TrabajadorListCtrl', ['$scope', 'TrabajadorService',
    function($scope, TrabajadorService){
        $scope.modulo =
        {
            titulo : 'Administrar Trabajador',
            trabajadores : TrabajadorService.query()
        };

        $scope.modulo.datatable = {
            header : [  { id : 'id_trabajador', label : 'ID'},
                        { id : 'apellido_paterno', label : 'APELLIDO'},
                        { id : 'nombres', label : 'NOMBRE'},
                        { id : 'fecha_ingreso_planilla', label : 'INGRESO'}]
        }

    }]);

    return appControllers;

});
