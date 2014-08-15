(function(){

    'use strict';

    var appControllers = angular.module('appControllers',[]);

    appControllers.controller('MainCtrl',['$scope', 'MainService',
        function($scope, MainService){
            $scope.modulos = MainService.query();
    }]);

    appControllers.controller('PlanillaListCtrl',['$scope', 'Planilla',
        function($scope, Planilla){
            $scope.planilla = Planilla.query();
    }]);

})();
