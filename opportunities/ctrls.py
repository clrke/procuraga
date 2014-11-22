import requests
from procuraga.shortcuts import compact
from procuraga import query
from urllib.parse import urlparse
import statistics

def awards(request):
	award = requests.get('http://philgeps.cloudapp.net:5000/api/action/datastore_search_sql?sql='+
		query.get('539525df-fc9a-4adf-b33d-04747e95f120', int(request.GET['page']), int(request.GET['number']))).json()['result']['records']

	return compact("award")

def bids(request):
	bids = requests.get('http://philgeps.cloudapp.net:5000/api/action/datastore_search_sql?sql='+
		query.year('539525df-fc9a-4adf-b33d-04747e95f120', '2009')).json()
	return compact("bids")

def pperunit(request):
	pperunit = requests.get('http://philgeps.cloudapp.net:5000/api/action/datastore_search_sql?sql='+
		query.pperunit('daa80cd8-da5d-4b9d-bb6d-217a360ff7c1','2009','1000')).json()['result']['records']

	item_names = []

	[item_names.append(item['item_name']) for item in pperunit if item['item_name'] not in item_names]

	item_names.sort()

	items = []

	for item_name in item_names:
		item_count = len([item for item in pperunit if item['item_name'] == item_name])

		item_budgets = [int(item['budget'])/int(item['qty']) for item in pperunit if item['item_name'] == item_name]
		minimum = min(item_budgets)
		maximum = max(item_budgets)
		mean = statistics.mean(item_budgets)
		median = statistics.median(item_budgets)
		try:
			mode = statistics.mode(item_budgets)
		except statistics.StatisticsError:
			mode = "N/A"

		items.append({
			"item_name": item_name,
			"min": minimum,
			"max": maximum,
			"count": item_count,
			"mean" : mean,
			"median" : median,
			"mode" : mode
		})

	return compact("items")

def supplier(request):
	supplier = requests.get('http://api.data.gov.ph/api/action/datastore_search_sql?sql='+
		query.supplier('23de10e9-197e-4294-abd1-eba0188110cd','1000')).json()
	return compact("supplier")
