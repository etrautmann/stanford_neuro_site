from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # INDEX
    url(r'^$', 'main.views.home'),

    # about
    url(r'^about', 'main.views.about'),

    # prospective students
    url(r'^prospective_students', 'main.views.prospective_students'),

    # student profiles
    url(r'^students/profiles', 'main.views.student_profiles'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin', admin.site.urls),

    # catch all other URLs
    url(r'^', 'main.views.notfound', name='404'),
)
