'use strict'

require.config({
	baseUrl : 'static',
	paths : {
		'jquery' : 'vendor/jquery/jquery',
        'modernizr' : 'vendor/modernizr/modernizr',
		'foundation' : 'vendor/foundation/foundation',
		'angular' : 'vendor/angular/angular',
		'ngRoute' : 'vendor/angular-route/angular-route',
		'ngResource' : 'vendor/angular-resource/angular-resource',
		'app' : 'app/js/app',
		'appControllers' : 'app/js/modules/controllers',
		'appServices' : 'app/js/modules/services',
		'appDirectives' : 'app/js/modules/directives'
	},
	shim : {
		foundation : {
			deps : ['jquery'],
			exports : 'foundation'
		},
		angular : {
			deps : ['jquery'],
			exports : 'angular'
		},
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

require(['modernizr', 'jquery', 'foundation', 'angular', 'app'], function(){
    $(document).foundation();

    angular.bootstrap(angular.element(document), ['PerforadoraApp']);
});
