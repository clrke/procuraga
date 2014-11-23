angular.module 'Procuraga'
	.controller 'ResearchesCtrl', ['$http', '$scope', '$filter', ($http, $scope, $filter) ->
		r = this

		r.csort = 'item_name'
		r.asc = false

		r.csort2 = 'bidder'
		r.asc2 = false

		r.pageSize = 20
		r.currentPage = 1

		r.year = __year__

		r.items = []

		r.min = (instances) ->
			numbers = []
			for instance in instances
				numbers.push (instance.budget / instance.qty)

			return Math.min.apply null, numbers

		r.max = (instances) ->
			numbers = []
			for instance in instances
				numbers.push (instance.budget / instance.qty)

			return Math.max.apply null, numbers


		$http.get('/api/pperunit?year='+r.year).success (data) ->
			r.items = data.items
			r.currentPage = 1
			r.loaded = true

		r.ceil = window.Math.ceil;

		$scope.$watch angular.bind(r, -> r.search),
		(value) ->
			if r.currentPage > r.ceil($filter('filter')(r.items, value).length / r.pageSize)
				r.currentPage = r.ceil($filter('filter')(r.items, value).length / r.pageSize)
			if r.ceil($filter('filter')(r.items, value).length / r.pageSize) != 0 and r.currentPage < 1
				r.currentPage = 1

		"of the jedi"
	]
	.filter('startFrom', ->
		(input, start) ->
		    start = +start
		    input.slice (start)
		)

