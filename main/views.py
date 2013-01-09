# Create your views here.
from django.http import HttpResponse
from main.models import Student, Faculty, Alumnus, Course, Theme, FAQ, Library
from django.template import RequestContext
from django.shortcuts import render_to_response
import datetime, os, string

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

def contact(request):
    return render_to_response('about/contact.html', [], context_instance=RequestContext(request))


### Prospective Students ###
def program_of_study(request):
    return render_to_response('prospective_students/program_of_study.html', [], context_instance=RequestContext(request))

def why_stanford(request):
    return render_to_response('prospective_students/why_stanford.html', [], context_instance=RequestContext(request))

def meet_current_students(request):
    return render_to_response('prospective_students/meet_current_students.html', [], context_instance=RequestContext(request))

def getFAQ(request):
    return render_to_response('prospective_students/FAQ.html', context_instance=RequestContext(request))

def admissions(request):
    return render_to_response('prospective_students/admissions.html', [], context_instance=RequestContext(request))

def funding_opportunities(request):
    return render_to_response('prospective_students/funding_opportunities.html', [], context_instance=RequestContext(request))

def diversity(request):
    return render_to_response('prospective_students/diversity.html', [], context_instance=RequestContext(request))

def contact_us(request):
    return render_to_response('prospective_students/contact_us.html', [], context_instance=RequestContext(request))

def how_to_apply(request):
    return render_to_response('prospective_students/how_to_apply.html', [], context_instance=RequestContext(request))



### Students ###
def student_profiles(request):
    return render_to_response('students/profiles.html', {'students': Student.objects.all()}, context_instance=RequestContext(request))

def student_profiles_new(request):
    return render_to_response('students/profiles_new.html', {'students': Student.objects.all()}, context_instance=RequestContext(request))

def alumni_profiles(request):
    return render_to_response('students/alumni.html', {'alumni': Alumnus.objects.all()}, context_instance=RequestContext(request))

def library(request):
    return render_to_response('students/library.html', {'books': Library.objects.all()}, context_instance=RequestContext(request))

def student_intranet(request):
    return render_to_response('students/intranet.html', {'students': Student.objects.all()}, context_instance=RequestContext(request))

def photos(request):
    return render_to_response('students/photos.html', {'students': Student.objects.all()}, context_instance=RequestContext(request))

def courses(request):
    # all courses
    allcourses = Course.objects.all()
    # systems/behavioral/computational
    sys = Course.objects.filter(Area_Fulfill__exact='Systems/Behavioral/Computational')
    # translational
    trans = Course.objects.filter(Area_Fulfill__exact='Translational')
    # cellular/molecular/developmental
    cellmol = Course.objects.filter(Area_Fulfill__exact='Cellular/Molecular/Developmental')
    # none
    none = Course.objects.filter(Area_Fulfill__exact='none')
    # get year
    lastyearstr = str(datetime.datetime.now().year-1)
    thisyearstr = str(datetime.datetime.now().year)
    nextyearstr = str(datetime.datetime.now().year+1)
    nextnextyearstr = str(datetime.datetime.now().year+2)
    month = datetime.datetime.now().month
    if month < 6:
	tystr = lastyearstr + '-' + thisyearstr[2:4]
	nystr = thisyearstr + '-' + nextyearstr[2:4]
    else:
	tystr = thisyearstr + '-' + nextyearstr[2:4]
	nystr = nextyearstr + '-' + nextnextyearstr[2:4]
    # this year
    thisyear = Course.objects.filter(Next_Offered__exact=tystr).exclude(Area_Fulfill__exact='none')
    nextyear = Course.objects.filter(Next_Offered__exact=nystr).exclude(Area_Fulfill__exact='none')

    # course matrix (autumn)
    tyma = Course.objects.filter(Area_Fulfill__exact='Cellular/Molecular/Developmental',Next_Offered__exact=tystr,Quarter_Offered__exact='Autumn')
    tyta = Course.objects.filter(Area_Fulfill__exact='Translational',Next_Offered__exact=tystr,Quarter_Offered__exact='Autumn')
    tysa = Course.objects.filter(Area_Fulfill__exact='Systems/Behavioral/Computational',Next_Offered__exact=tystr,Quarter_Offered__exact='Autumn')
    nyma = Course.objects.filter(Area_Fulfill__exact='Cellular/Molecular/Developmental',Next_Offered__exact=nystr,Quarter_Offered__exact='Autumn')
    nyta = Course.objects.filter(Area_Fulfill__exact='Translational',Next_Offered__exact=nystr,Quarter_Offered__exact='Autumn')
    nysa = Course.objects.filter(Area_Fulfill__exact='Systems/Behavioral/Computational',Next_Offered__exact=nystr,Quarter_Offered__exact='Autumn')

    # course matrix (winter)
    tymw = Course.objects.filter(Area_Fulfill__exact='Cellular/Molecular/Developmental',Next_Offered__exact=tystr,Quarter_Offered__exact='Winter')
    tytw = Course.objects.filter(Area_Fulfill__exact='Translational',Next_Offered__exact=tystr,Quarter_Offered__exact='Winter')
    tysw = Course.objects.filter(Area_Fulfill__exact='Systems/Behavioral/Computational',Next_Offered__exact=tystr,Quarter_Offered__exact='Winter')
    nymw = Course.objects.filter(Area_Fulfill__exact='Cellular/Molecular/Developmental',Next_Offered__exact=nystr,Quarter_Offered__exact='Winter')
    nytw = Course.objects.filter(Area_Fulfill__exact='Translational',Next_Offered__exact=nystr,Quarter_Offered__exact='Winter')
    nysw = Course.objects.filter(Area_Fulfill__exact='Systems/Behavioral/Computational',Next_Offered__exact=nystr,Quarter_Offered__exact='Winter')

    # course matrix (spring)
    tyms = Course.objects.filter(Area_Fulfill__exact='Cellular/Molecular/Developmental',Next_Offered__exact=tystr,Quarter_Offered__exact='Spring')
    tyts = Course.objects.filter(Area_Fulfill__exact='Translational',Next_Offered__exact=tystr,Quarter_Offered__exact='Spring')
    tyss = Course.objects.filter(Area_Fulfill__exact='Systems/Behavioral/Computational',Next_Offered__exact=tystr,Quarter_Offered__exact='Spring')
    nyms = Course.objects.filter(Area_Fulfill__exact='Cellular/Molecular/Developmental',Next_Offered__exact=nystr,Quarter_Offered__exact='Spring')
    nyts = Course.objects.filter(Area_Fulfill__exact='Translational',Next_Offered__exact=nystr,Quarter_Offered__exact='Spring')
    nyss = Course.objects.filter(Area_Fulfill__exact='Systems/Behavioral/Computational',Next_Offered__exact=nystr,Quarter_Offered__exact='Spring')

    return render_to_response('students/courses.html', {'noncore': Course.objects.filter(Area_Fulfill__exact='none'), 'courses': allcourses, 'syscomp': sys, 'trans': trans, 'cellmol': cellmol, 'none': none, 'thisyear': thisyear, 'nextyear': nextyear, 'tyma': tyma, 'tyta': tyta, 'tysa': tysa, 'nyma': nyma, 'nyta': nyta, 'nysa': nysa, 'tymw': tymw, 'tytw': tytw, 'tysw': tysw, 'nymw': nymw, 'nytw': nytw, 'nysw': nysw, 'tyms': tyms, 'tyts': tyts, 'tyss': tyss, 'nyms': nyms, 'nyts': nyts, 'nyss': nyss}, context_instance=RequestContext(request))

def calendar(request):
    return render_to_response('students/calendar.html', {'students': Student.objects.all()}, context_instance=RequestContext(request))

def news(request):
    return render_to_response('students/news.html', {'students': Student.objects.all()}, context_instance=RequestContext(request))



#### News and Media ###
#def publications(request):
    #return render_to_response('media/publications.html', [], context_instance=RequestContext(request))
#
def upcoming_events(request):
    return render_to_response('news_media/upcoming_events.html', [], context_instance=RequestContext(request))

def announcements(request):
    allfiles = os.listdir('/home/ross/public_html/ProgramDocuments')
    files = []
    #names = []
    for file in allfiles:
	if file.endswith('pdf') or file.endswith('PDF'):
	    files.append({'file': file, 'name': string.replace(file,'_',' ')})
	    #names.append(string.replace(file,'_',' '))

    variables = RequestContext(request,{
	#'names' : names,
        'files' : files
	#files: {'files': files, 'names': names}
    })

    return render_to_response('news_media/announcements.html', variables, context_instance=RequestContext(request))

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
    abspath = open('/Users/nirum/Dropbox/neuro/main/static/handbook.pdf','r')
    response = HttpResponse(content=abspath.read())
    response['Content-Type']= 'application/pdf'
    response['Content-Disposition'] = 'attachment; filename=%s.pdf' \
                                       % 'Stanford Neuroscience Program Handbook'
    return response

### Faculty ###
def faculty_profiles(request):
		faculty_split = {}
		faculty_split['Disease'] = Faculty.objects.filter(mentor=1).filter(Disease=1)
		faculty_split['Systems'] = Faculty.objects.filter(mentor=1).filter(Systems=1)
		faculty_split['Cellular'] = Faculty.objects.filter(mentor=1).filter(Cellular=1)
		faculty_split['Molecular'] = Faculty.objects.filter(mentor=1).filter(Molecular=1)
		faculty_split['Excitability'] = Faculty.objects.filter(mentor=1).filter(Excitability=1)
		faculty_split['Developmental'] = Faculty.objects.filter(mentor=1).filter(Developmental=1)
		faculty_split['Computational'] = Faculty.objects.filter(mentor=1).filter(Computational=1)

		return render_to_response('faculty/profiles.html', {'faculty': Faculty.objects.filter(mentor=1), 'fsplit': faculty_split}, context_instance=RequestContext(request))

def faculty_instructors(request):
		faculty_split = {}
		faculty_split['Disease'] = Faculty.objects.filter(mentor=0).filter(Disease=1)
		faculty_split['Systems'] = Faculty.objects.filter(mentor=0).filter(Systems=1)
		faculty_split['Cellular'] = Faculty.objects.filter(mentor=0).filter(Cellular=1)
		faculty_split['Molecular'] = Faculty.objects.filter(mentor=0).filter(Molecular=1)
		faculty_split['Excitability'] = Faculty.objects.filter(mentor=0).filter(Excitability=1)
		faculty_split['Developmental'] = Faculty.objects.filter(mentor=0).filter(Developmental=1)
		faculty_split['Computational'] = Faculty.objects.filter(mentor=0).filter(Computational=1)

		return render_to_response('faculty/instructors.html', {'faculty': Faculty.objects.filter(mentor=0), 'fsplit': faculty_split}, context_instance=RequestContext(request))
