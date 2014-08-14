module.exports = function(grunt){
    grunt.initConfig({
        pkg : grunt.file.readJSON('package.json'),
        jshint : {
            options : {
                jshintrc : true,
                reporter : require('jshint-stylish'),
            },
            all : ['perforadora/static/js/app/**/*.js'],
        },
        watch : {
            files : ['perforadora/static/js/app/**/*.js'],
            tasks : ['jshint'],
        },
        bower: {
            install: {
                options: {
                    targetDir: './perforadora/static/vendor',
                    layout:'byType',
                    install: true,
                    verbose: false,
                    cleanTargetDir: false,
                    cleanBowerDir: false,
                    bowerOptions: {}
                }
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-jshint');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-bower-task');

    grunt.registerTask('default',['jshint', 'watch']);
};
