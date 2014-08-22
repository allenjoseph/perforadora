(function(){

    'use strict';

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
            $scope.modulos = MenuService.query();
        }]);

})();
