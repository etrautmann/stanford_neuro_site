# Create your views here.
from django.http import HttpResponse
from main.models import Student, Faculty
from django.template import RequestContext
from django.shortcuts import render_to_response

### Other ###
def notfound(request):
    return render_to_response('404.html', [], context_instance=RequestContext(request))

def home(request): 
    return render_to_response('index.html', [], context_instance=RequestContext(request))



### About ###
def about(request):
    return render_to_response('about/info.html', [], context_instance=RequestContext(request))

def handbook(request):
    return render_to_response('about/handbook.html', [], context_instance=RequestContext(request))



### Prospective Students ###
def program_of_study(request):
    return render_to_response('prospective_students/program_of_study.html', [], context_instance=RequestContext(request))

def why_stanford(request):
    return render_to_response('prospective_students/why_stanford.html', [], context_instance=RequestContext(request))

def meet_current_students(request):
    return render_to_response('prospective_students/meet_current_students.html', [], context_instance=RequestContext(request))

def FAQ(request):
    return render_to_response('prospective_students/FAQ.html', [], context_instance=RequestContext(request))

def admissions(request):
    return render_to_response('prospective_students/admissions.html', [], context_instance=RequestContext(request))

def funding_opportunities(request):
    return render_to_response('prospective_students/funding_opportunities.html', [], context_instance=RequestContext(request))

def contact_us(request):
    return render_to_response('prospective_students/contact_us.html', [], context_instance=RequestContext(request))

def apply_now(request):
    return render_to_response('prospective_students/apply_now.html', [], context_instance=RequestContext(request))



### Students ###
def student_profiles(request):
    return render_to_response('students/profiles.html', {'students': Student.objects.all()}, context_instance=RequestContext(request))

def student_intranet(request):
    return render_to_response('students/intranet.html', {'students': Student.objects.all()}, context_instance=RequestContext(request))

def photos(request):
    return render_to_response('students/photos.html', {'students': Student.objects.all()}, context_instance=RequestContext(request))

def courses(request):
    return render_to_response('students/courses.html', {'students': Student.objects.all()}, context_instance=RequestContext(request))

def calendar(request):
    return render_to_response('students/calendar.html', {'students': Student.objects.all()}, context_instance=RequestContext(request))

def news(request):
    return render_to_response('students/news.html', {'students': Student.objects.all()}, context_instance=RequestContext(request))



#### News and Media ###
#def publications(request):
    #return render_to_response('media/publications.html', [], context_instance=RequestContext(request))
#
#def calendar_of_events(request):
    #return render_to_response('media/calendar_of_events.html', [], context_instance=RequestContext(request))
#
#def press_releases(request):
    #return render_to_response('media/press_releases.html', [], context_instance=RequestContext(request))
#
#def twitter(request):
    #return render_to_response('media/twitter.html', [], context_instance=RequestContext(request))
#
#def neuroblog(request):
    #return render_to_response('media/neuroblog.html', [], context_instance=RequestContext(request))


### Other ###
def download_handbook(request): 
    abspath = open('/Users/Niru/Sites/stanford_neuro_site/main/static/handbook.pdf','r')
    response = HttpResponse(content=abspath.read())
    response['Content-Type']= 'application/pdf'
    response['Content-Disposition'] = 'attachment; filename=%s.pdf' \
                                       % 'Stanford Neuroscience Program Handbook'
    return response

### Faculty ###
def faculty_profiles(request):
    return render_to_response('faculty/profiles.html', {'faculty': Faculty.objects.all()}, context_instance=RequestContext(request))
