from procuraga.shortcuts import compact

def home(request):
	year = request.GET['year'] if 'year' in request.GET else None
	return compact("year")
