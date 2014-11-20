from django.shortcuts import render
from . import ctrls
# Create your views here.
def home(request): return render(request, "index.html", ctrls.home(request))
