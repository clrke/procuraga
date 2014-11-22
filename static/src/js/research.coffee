angular.module 'Procuraga'
	.controller 'ResearchesCtrl', ['$http', '$scope', ($http) ->
		r = this

		r.csort = 'item_name'
		r.asc = false

		r.pageSize = 20
		r.currentPage = 1

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

		$http.get '/api/pperunit'
			.success (data) ->
				r.items = data.items
				r.currentPage = 1

		r.ceil = window.Math.ceil;

		"of the jedi"
	]
	.filter('startFrom', ->
		(input, start) ->
		    start = +start
		    input.slice (start)
		)

