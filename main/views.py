# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def notfound(request):
    return render_to_response('404.html', [], context_instance=RequestContext(request))

# def base(request):
    # return render_to_response('base.html', [], context_instance=RequestContext(request))

def programinfo(request):
    return render_to_response('programinfo.html', [], context_instance=RequestContext(request))

def about(request):
    return render_to_response('about.html', [], context_instance=RequestContext(request))

def home(request): 
    return render_to_response('index.html', [], context_instance=RequestContext(request))
