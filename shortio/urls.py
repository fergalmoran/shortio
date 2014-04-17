from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'shortio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'shorts.views.index'),
    url(r'^shorts/', include('shorts.urls', namespace='urls')),
    url(r'^api/', include('shorts.urls', namespace='api')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<dispatch_id>\w+)/$', 'dispatcher.views.dispatch'),
)
