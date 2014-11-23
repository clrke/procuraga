from django.http import JsonResponse
from django.shortcuts import render
from . import ctrls

def home(request): 		return render(request, "index.html", {"active" : "home"})
def awards(request): 	return JsonResponse(ctrls.awards(request))
def bids(request): 		return JsonResponse(ctrls.bids(request))
def pperunit(request):	return JsonResponse(ctrls.pperunit(request))
