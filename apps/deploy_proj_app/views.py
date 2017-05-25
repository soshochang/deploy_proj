from django.shortcuts import render

from .models import Dojo
# Create your views here.

def index(request):
	context = {
		"dojo" : Dojo.objects.all()
	}
	return render(request, "deploy_proj_app/index.html", context)
