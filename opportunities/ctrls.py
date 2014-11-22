import requests
from procuraga.shortcuts import compact
from procuraga import query
from urllib.parse import urlparse

def awards(request):
	award = requests.get('http://philgeps.cloudapp.net:5000/api/action/datastore_search_sql?sql='+
		query.get('539525df-fc9a-4adf-b33d-04747e95f120', int(request.GET['page']), int(request.GET['number']))).json()['result']['records']

	return compact("award")

def bids(request):
	bids = requests.get('http://philgeps.cloudapp.net:5000/api/action/datastore_search_sql?sql='+
		query.year('539525df-fc9a-4adf-b33d-04747e95f120', '2009')).json()
	print(query.year('baccd784-45a2-4c0c-82a6-61694cd68c9d', '2%'))
	return compact("bids")

def pperunit(request):
	pperunit = requests.get('http://philgeps.cloudapp.net:5000/api/action/datastore_search_sql?sql='+
		query.pperunit('daa80cd8-da5d-4b9d-bb6d-217a360ff7c1','2009',5)).json()
	return compact("pperunit")
