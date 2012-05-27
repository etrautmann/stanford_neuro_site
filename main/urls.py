from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('main.views',
    # INDEX
    url(r'^$', 'home'),

    # about
    url(r'^about', 'about'),

    # prospective students
    url(r'^prospective_students', 'prospective_students'),

    ### Student ###
    url(r'^students/profiles', 'student_profiles'),
    url(r'^students/intranet', 'student_intranet'),
    url(r'^students/courses', 'courses'),
    url(r'^students/photos', 'photos'),
    url(r'^students/events', 'calendar'),
    #url(r'^students/news', 'news'),
    
    ### Faculty ###
    url(r'^faculty/profiles', 'faculty_profiles'),
    #url(r'^faculty/intranet', 'faculty_intranet'),

    ### News & Media ###
    #url(r'^media/publications', 'publications'),
    #url(r'^media/press', 'press'),
)

urlpatterns += patterns('',
    ### Admin and Other ###
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin', admin.site.urls),

    # catch all other URLs (this must be last!)
    url(r'^', 'main.views.notfound', name='404'),
)
