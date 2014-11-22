from django.shortcuts import render
from . import ctrls

def home(request):
	return render(request, "research_index.html", ctrls.home(request))
