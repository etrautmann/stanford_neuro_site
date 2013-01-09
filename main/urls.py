from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('main.views',
    # INDEX
    url(r'^$', 'home'),

    # about
    url(r'^about/info', 'about'),
    url(r'^about/contact', 'contact'),

    # prospective students
    #url(r'^prospective_students', 'prospective_students'),
    url(r'^prospective_students/why_stanford', 'why_stanford'),
    url(r'^prospective_students/program_of_study', 'program_of_study'),
    url(r'^prospective_students/meet_current_students', 'meet_current_students'),
    url(r'^prospective_students/FAQ', 'getFAQ'),
    url(r'^prospective_students/admissions', 'admissions'),
    url(r'^prospective_students/diversity', 'diversity'),
    url(r'^prospective_students/funding_opportunities', 'funding_opportunities'),
    url(r'^prospective_students/contact_us', 'contact_us'),
    url(r'^prospective_students/how_to_apply', 'how_to_apply'),

    ### Student ###
    url(r'^students/profiles_new', 'student_profiles_new'),
    url(r'^students/profiles', 'student_profiles'),
    url(r'^alumni/profiles', 'alumni_profiles'),
    url(r'^students/library', 'library'),
    url(r'^students/intranet', 'student_intranet'),
    url(r'^students/courses', 'courses'),
    url(r'^students/photos', 'photos'),
    url(r'^students/events', 'calendar'),
    #url(r'^students/news', 'news'),

    ### Faculty ###
    url(r'^faculty/profiles', 'faculty_profiles'),
    url(r'^faculty/instructors', 'faculty_instructors'),
    #url(r'^faculty/intranet', 'faculty_intranet'),

    ### News & Media ###
    #url(r'^media', 'media'),
    #url(r'^media/publications', 'publications'),
    url(r'^news_media/upcoming_events', 'upcoming_events'),
    url(r'^news_media/announcements', 'announcements'),
    url(r'^ProgramDocuments', 'announcements'),
    #url(r'^media/press_releases', 'press_releases'),
    #url(r'^media/twitter', 'twitter'),
    #url(r'^media/neuroblog', 'neuroblog'),
)

urlpatterns += patterns('',
    ### Admin and Other ###
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin', admin.site.urls),

    # catch all other URLs (this must be last!)
    url(r'^', 'main.views.notfound', name='404'),
)
