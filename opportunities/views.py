from django.http import JsonResponse
from django.shortcuts import render
from . import ctrls

def home(request): 			return render(request, "index.html")
def activities(request): 	return JsonResponse(ctrls.activities(request))
