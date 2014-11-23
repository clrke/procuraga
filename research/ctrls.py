from procuraga.shortcuts import compact

def home(request):
	year = request.GET['year'] if 'year' in request.GET else None
	active = "research"
	return compact("year", "active")
