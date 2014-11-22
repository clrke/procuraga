angular.module 'Procuraga'
	.controller 'OpportunitiesCtrl', ['$http', '$scope', ($http) ->
		opp = this

		$http.get '/api/activities'
			.success (data) ->
				opp.awards = data.awards

		$http.get '/api/bids'
			.success (data) ->
				opp.bids = data.bids

		"of the jedi"
	]
