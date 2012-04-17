from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # INDEX
    url(r'^$', 'main.views.home'),

    # url(r'^main/', include('main.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    # program info
    url(r'^programinfo', 'main.views.programinfo'),

    # about
    url(r'^about', 'main.views.about'),

    # catch all other URLs
    url(r'^', 'main.views.notfound', name='404'),
)
