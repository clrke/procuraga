import requests

def home(request):
	activities = requests.get('http://student-journal.eu1.frbit.net/activities').json()
	return {"activities": activities}
