/**
 * Created by jv on 13/03/2014.
 */
var job_app = angular.module('job_app', ['ngRoute']);

job_app.config(['$routeProvider', function($routeProvider) {
    $routeProvider.
        when('/',{templateUrl: '/static/views/index.html', controller: IndexCtrl}).

        when('/employer/',{templateUrl: '/static/views/employer_index.html', controller: EmployerIndexCtrl}).

        when('/create/ad/',{templateUrl: '/static/views/create_ad.html', controller: CreateAdCtrl}).

//        when('/add/project/',{templateUrl: '/static/views/add_project.html', controller: AddProjectCtrl}).
//        when('/student/:id',{templateUrl: '/static/views/view_student.html', controller: ViewStudentCtrl}).
        otherwise({redirectTo: '/'});

}]);