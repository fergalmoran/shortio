'use strict';

angular.module('shortioApp')
    .controller('UrlCtrl', function ($scope, urlResource) {
        function checkUrl(s) {
            var regexp = /(ftp|http|https):\/\/(\w+:{0,1}\w*@)?(\S+)(:[0-9]+)?(\/|\/([\w#!:.?+=&%@!\-\/]))?/;
            return regexp.test(s);
        }

        $scope.shortenUrl = function () {
            $scope.error = "";
            $scope.shortened_url = "";
            if (checkUrl($scope.url)) {
                var newUrl = new urlResource({url: $scope.url});
                newUrl.$save()
                    .then(function (result) {
                        $scope.shortened_url = result.shortened_url;
                    });
            } else {
                $scope.error = "Not a valid url";
            }
        };
        $('#url').focus();
    });
