from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def IndexView(request):
    template = loader.get_template('members/index.html')
    return HttpResponse(template.render({},request))