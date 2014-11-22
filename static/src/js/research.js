// Generated by CoffeeScript 1.8.0
(function() {
  angular.module('Procuraga').controller('ResearchesCtrl', [
    '$http', '$scope', '$filter', function($http, $scope, $filter) {
      var r;
      r = this;
      r.csort = 'item_name';
      r.asc = false;
      r.pageSize = 20;
      r.currentPage = 1;
      r.min = function(instances) {
        var instance, numbers, _i, _len;
        numbers = [];
        for (_i = 0, _len = instances.length; _i < _len; _i++) {
          instance = instances[_i];
          numbers.push(instance.budget / instance.qty);
        }
        return Math.min.apply(null, numbers);
      };
      r.max = function(instances) {
        var instance, numbers, _i, _len;
        numbers = [];
        for (_i = 0, _len = instances.length; _i < _len; _i++) {
          instance = instances[_i];
          numbers.push(instance.budget / instance.qty);
        }
        return Math.max.apply(null, numbers);
      };
      $http.get('/api/pperunit').success(function(data) {
        r.items = data.items;
        return r.currentPage = 1;
      });
      r.ceil = window.Math.ceil;
      $scope.$watch(angular.bind(r, function() {
        return r.search;
      }), function(value) {
        if (r.currentPage > r.ceil($filter('filter')(r.items, value).length / r.pageSize)) {
          r.currentPage = r.ceil($filter('filter')(r.items, value).length / r.pageSize);
        }
        if (r.ceil($filter('filter')(r.items, value).length / r.pageSize) !== 0 && r.currentPage < 1) {
          return r.currentPage = 1;
        }
      });
      return "of the jedi";
    }
  ]).filter('startFrom', function() {
    return function(input, start) {
      start = +start;
      return input.slice(start);
    };
  });

}).call(this);
