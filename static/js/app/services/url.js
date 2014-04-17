'use strict'

angular.module('shortioApp')
    .factory('urlResource', function ($resource) {
        return $resource('/api/urls/:id', {id: '@id'});
    });
