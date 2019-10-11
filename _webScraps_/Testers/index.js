(function (angular) {
    "use strict";
    angular.module("testApp", ['ngAnimate', 'ngSanitize'])
        // .factory('CoilUserServc', function ($http) {
        //     var facw = {};
        //     facw.GetAllUsers = function () { return $http.get('/Coil/GetAllUserds'); };
        //     return facw;
        // })
        // .factory('MiniService', function ($http) {
        //     var fac = {};
        //     fac.GetAllSizes = function () { return $http.get('/Coil/GetAllSizesMini'); };
        //     return fac;
        // })        
        .controller("testCtrl", ['$scope', '$http', '$location', '$window', '$log', function ($scope, $http, $location, $window, $log) {
            

           

        }]);



    //}).config(function ($logProvider) {
    //    $logProvider.debugEnabled(false);
    //}).run(function ($rootScope, $log) {
    //$rootScope.$log = $log;

    //}).filter('unique', function () {
    //    // we will return a function which will take in a collection
    //    // and a keyname
    //    return function (collection, keyname) {
    //        // we define our output and keys array;
    //        var output = [],
    //            keys = [];

    //        // we utilize angular's foreach function
    //        // this takes in our original collection and an iterator function
    //        angular.forEach(collection, function (item) {
    //            // we check to see whether our object exists
    //            var key = item[keyname];
    //            // if it's not already part of our keys array
    //            if (keys.indexOf(key) === -1) {
    //                // add it to our keys array
    //                keys.push(key);
    //                // push this item to our final output array
    //                output.push(item);
    //            }
    //        });
    //        // return our array which should be devoid of
    //        // any duplicates
    //        return output;
    //    };
}(window.angular));