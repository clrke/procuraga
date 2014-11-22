angular.module 'Procuraga'
	.controller 'ResearchesCtrl', ['$http', '$scope', ($http) ->
		r = this
		r.items = [
			{"item_name":"plywood", "instances":[
				{"budget": 20, "qty": 5}
				{"budget": 120, "qty": 5}
				{"budget": 320, "qty": 5}
				{"budget": 420, "qty": 5}
				{"budget": 520, "qty": 5}
			]}
			{"item_name":"something else", "instances":[
				{"budget": 500, "qty": 6}
				{"budget": 1600, "qty": 6}
				{"budget": 3600, "qty": 6}
				{"budget": 4600, "qty": 6}
				{"budget": 6600, "qty": 6}
			]}
		]

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

		# $http.get '/api/items'
		# 	.success (data) ->
		# 		r.items = data.items


		"of the jedi"
	]
