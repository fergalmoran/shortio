from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from models import Url
# Create your views here.


def index(request, error=None):
    latest_url_list = Url.objects.order_by('-date_created')[:5]
    context = {'latest_url_list': latest_url_list, 'error_message': error}
    return render(request, 'index.html', context)


def detail(request, url_id):
    url = get_object_or_404(Url, pk=url_id)
    return render(request, 'detail.html', {'url': url})


def create(request):
    try:
        u = Url(url=request.POST['url'])
        u.save()
    except Exception, ex:
        return index(request, error=ex.message)
    else:
        return HttpResponseRedirect(reverse('urls:index'))
