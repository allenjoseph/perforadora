'use strict'

require.config({
	baseUrl : 'static',
	paths : {
		'angular' : 'vendor/angular/angular',
		'ngRoute' : 'vendor/angular-route/angular-route',
		'ngResource' : 'vendor/angular-resource/angular-resource',
		'app' : 'app/js/app',
		'appControllers' : 'app/js/modules/controllers',
		'appServices' : 'app/js/modules/services',
		'appDirectives' : 'app/js/modules/directives'
	},
	shim : {
		ngRoute : {
			deps : ['angular'],
			exports : 'angular'
		},
		ngResource : {
			deps : ['angular'],
			exports : 'angular'
		}
	}
});

require(['angular', 'app'], function(){
    angular.bootstrap(angular.element(document), ['PerforadoraApp']);
});
