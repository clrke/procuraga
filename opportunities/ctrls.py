import requests
from procuraga.shortcuts import compact

def home(request):
	activities = requests.get('http://student-journal.eu1.frbit.net/activities').json()
	return compact("activities")
