from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core import serializers
from skripte.models import Equation
import json

# Create your views here.

@login_required(login_url='/admin/login/')
def IndexView(request, *args, **kwargs):
    return render(request, 'frontend/index.html')



def AlpineView(request, *args, **kwargs):
    queryset = Equation.objects.all()
    queryset_json = serializers.serialize('json', queryset)
    return render(request, 'frontend/alpine.html', { 'equations': queryset_json })