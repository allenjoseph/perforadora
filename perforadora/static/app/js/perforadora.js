(function(){
    'use strict';

    var perforadoraApp = angular.module('perforadoraApp',[]);

    perforadoraApp.controller('mainCtrl', function($scope){
    	$scope.modulos = [{ruta : '/' , nombre : 'Home'},
    	{ruta : 'trabajador' , nombre : 'Trabajador'},
    	{ruta : 'prestamo' , nombre : 'Prestamo'},
    	{ruta : 'dia' , nombre : 'Dia'},
    	{ruta : 'semama' , nombre : 'Semana'},
    	{ruta : 'planilla' , nombre : 'Planilla'}];
    });
})();

