from django.conf.urls import url, patterns


urlpatterns = patterns(
    url(r'^(?P<dispatch_id>\w+)/$', 'dispatcher.views.dispatch'),
)
