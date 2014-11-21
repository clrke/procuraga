from django.shortcuts import render
from . import ctrls

def home(request): return render(request, "index.html", ctrls.home(request))
