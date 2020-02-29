# created by -Ritesh
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name':'Ritesh','place':'Mars'}
    return render(request, 'index.html', params)
    # return HttpResponse('<h1><a href="#">Home</a></h1>')

def removepunc(request):
    return HttpResponse('remove punc')

def capfirst(request):
    return HttpResponse('captalizefirst')

def newlineremove(request):
    return HttpResponse('remove new line')

def removespace(request):
    return HttpResponse('removespace')

def charcount(request):
    return HttpResponse('charcount')