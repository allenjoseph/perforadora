'use strict';

define(['angular'],function(){

    var appDirectives = angular.module('appDirectives',[]);

    appDirectives.directive('appMenu', function(){
        return {
            restrict : 'E',
            templateUrl : 'static/partials/nav.tpl.html'
        };
    });

    appDirectives.directive('appMenuOption', function(){
        return{
            restrict: 'A',
            link: function(scope,element,attrs){
                var self = scope;
                element.on('click', function(){
                    for(var i=0, len=self.modulos.length; i < len; i++ ){
                        if(self.modulos[i].activo === 'true'){
                            self.modulos[i].activo = 'false';
                        }
                    }
                    self.modulo.activo = 'true';
                });

                self.$watch('modulo.activo', function(value){
                    if(value === 'true'){
                        element.addClass('unavailable');
                    }else{
                        element.removeClass('unavailable');
                    }
                });
            }
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
