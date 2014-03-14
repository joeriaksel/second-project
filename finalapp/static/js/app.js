/**
 * Created by jv on 13/03/2014.
 */
var job_app = angular.module('job_app', ['ngRoute']);

job_app.config(['$routeProvider', function($routeProvider) {
    $routeProvider.
        when('/',{templateUrl: '/static/views/index.html', controller: IndexCtrl}).

        when('/employer/activity/',{templateUrl: '/static/views/employer_activity.html', controller: EmployerActivityCtrl}).
        when('/employer/create/ad/',{templateUrl: '/static/views/employer_create_ad.html', controller: EmployerCreateAdCtrl}).
        when('/employer/edit/profile/',{templateUrl: '/static/views/employer_edit_profile.html', controller: EmployerEditProfileCtrl}).
        when('/employer/',{templateUrl: '/static/views/employer_index.html', controller: EmployerIndexCtrl}).
        when('/employer/message/worker/',{templateUrl: '/static/views/employer_message_worker.html', controller: EmployerMessageWorkerCtrl}).
        when('/employer/view/ad/:id',{templateUrl: '/static/views/employer_view_ad.html', controller: EmployerViewAdCtrl}).
        when('/employer/view/ads/',{templateUrl: '/static/views/employer_view_ads.html', controller: EmployerViewAdsCtrl}).
        when('/employer/view/message/:id',{templateUrl: '/static/views/employer_view_message.html', controller: EmployerViewMessageCtrl}).
        when('/employer/view/profile/',{templateUrl: '/static/views/employer_view_profile.html', controller: EmployerViewProfileCtrl}).
        when('/employer/view/worker/profile/:id',{templateUrl: '/static/views/employer_view_worker_profile.html', controller: EmployerViewWorkerProfileCtrl}).
        when('/employer/view/workers/',{templateUrl: '/static/views/employer_view_workers.html', controller: EmployerViewWorkersCtrl}).

        when('/worker/activity/',{templateUrl: '/static/views/worker_activity.html', controller: WorkerActivityCtrl}).
        when('/worker/edit/profile/',{templateUrl: '/static/views/worker_edit_profile.html', controller: WorkerEditProfileCtrl}).
        when('/worker/',{templateUrl: '/static/views/worker_index.html', controller: WorkerIndexCtrl}).
        when('/worker/message/employer/',{templateUrl: '/static/views/worker_message_employer.html', controller: WorkerMessageEmployerCtrl}).
        when('/worker/view/ad/:id',{templateUrl: '/static/views/worker_view_ad.html', controller: WorkerViewAdCtrl}).
        when('/worker/view/ads/:id',{templateUrl: '/static/views/worker_view_ads.html', controller: WorkerViewAdsCtrl}).
        when('/worker/view/categories/',{templateUrl: '/static/views/worker_view_categories.html', controller: WorkerViewCategoriesCtrl}).
        when('/worker/view/myjobs/',{templateUrl: '/static/views/worker_view_my_jobs.html', controller: WorkerViewMyJobsCtrl}).
        when('/worker/view/mymessages/',{templateUrl: '/static/views/worker_view_my_messages.html', controller: WorkerViewMyMessagesCtrl}).
        when('/worker/view/profile/',{templateUrl: '/static/views/worker_view_profile.html', controller: WorkerViewProfileCtrl}).

        otherwise({redirectTo: '/'});

}]);