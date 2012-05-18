# Create your views here.
from django.http import HttpResponse
from main.models import Student
from django.template import RequestContext
from django.shortcuts import render_to_response

def notfound(request):
    return render_to_response('404.html', [], context_instance=RequestContext(request))

def programinfo(request):
    return render_to_response('programinfo.html', [], context_instance=RequestContext(request))

def about(request):
    return render_to_response('about/about.html', [], context_instance=RequestContext(request))

def student_profiles(request):
    return render_to_response('students/profiles.html', {'students': Student.objects.all()}, context_instance=RequestContext(request))

def prospective_students(request):
    return render_to_response('prospective_students/prospective_students.html', [], context_instance=RequestContext(request))

def home(request): 
    return render_to_response('index.html', [], context_instance=RequestContext(request))
