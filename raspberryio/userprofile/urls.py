from django.conf.urls import patterns, include, url


urlpatterns = patterns('',

    # Mezzanine accounts urls (Put any custom ones above)
    url('^', include('mezzanine.accounts.urls')),
)