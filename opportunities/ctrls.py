import requests
from procuraga.shortcuts import compact
from procuraga import query

def awards(request):
	award = requests.get('http://philgeps.cloudapp.net:5000/api/action/datastore_search_sql?sql='+
		query.get('539525df-fc9a-4adf-b33d-04747e95f120', int(request.GET['page']), int(request.GET['number']))).json()['result']['records']

	return compact("award")

def bids(request):
	bids = requests.get('http://philgeps.cloudapp.net:5000/api/action/datastore_search_sql?sql='+
		query.year('baccd784-45a2-4c0c-82a6-61694cd68c9d', 2009)).json()
	return compact("bids")
