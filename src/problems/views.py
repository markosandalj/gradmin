from django.shortcuts import render
from django.http import HttpResponse
from .models import Problem, Section

# Create your views here.

def problems_list_view(request):
    problems_all = Problem.objects.all()
    sections_all = Section.objects.all()

    context = {
        'problems' : problems_all,
        'sections' : sections_all
    }
    return render(request, 'problems/problems_list.html', context=context)