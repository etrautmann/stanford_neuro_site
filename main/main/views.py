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

# def temp(request):
    # return render_to_response('components.html', [], context_instance=RequestContext(request))

# def test(request):
    # return render_to_response('test.html', [], context_instance=RequestContext(request))
