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
		query.pperunit('"daa80cd8-da5d-4b9d-bb6d-217a360ff7c1" as item, "baccd784-45a2-4c0c-82a6-61694cd68c9d" as bid, "ec10e1c4-4eb3-4f29-97fe-f09ea950cdf1" as org','2009','3000')).json()['result']['records']

	# return compact("pperunit")

	item_names = []

	[item_names.append(item['item_name']) for item in pperunit if item['item_name'] not in item_names]

	item_names.sort()

	items = []

	for item_name in item_names:
		item_budgets = [int(item['budget'])/int(item['qty']) for item in pperunit if item['item_name'] == item_name]

		business_categories = []
		[business_categories.append(item['business_category']) for item in pperunit if item['item_name'] == item_name and item['business_category'] not in business_categories]

		bidders = []
		[bidders.append([item['org_name'], item['publish_date']]) for item in pperunit if item['item_name'] == item_name and [item['org_name'], item['publish_date']] not in bidders]

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
			"count": len(bidders),
			"mean" : mean,
			"median" : median,
			"mode" : mode,
			"business_category" : business_categories,
			"bidders": bidders
		})

	return compact("items")
