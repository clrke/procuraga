// Generated by CoffeeScript 1.8.0
(function() {
  angular.module('Procuraga').controller('ResearchesCtrl', [
    '$http', '$scope', '$filter', function($http, $scope, $filter) {
      var r;
      r = this;
      r.csort = 'item_name';
      r.asc = false;
      r.csort2 = 'bidder';
      r.asc2 = false;
      r.pageSize = 20;
      r.currentPage = 1;
      r.year = __year__;
      r.items = [];
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
      $http.get('/api/pperunit?year=' + r.year).success(function(data) {
        r.items = data.items;
        r.currentPage = 1;
        return r.loaded = true;
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
