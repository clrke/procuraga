angular.module 'Procuraga'
	.controller 'OpportunitiesCtrl', ['$http', '$scope', ($http) ->
		opp = this

		$http.get '/api/activities'
			.success (data) ->
				opp.activities = data.activities

		"of the jedi"
	]
