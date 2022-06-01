from django.http import HttpResponse
from django.template import loader
from .models import extendsPractice


def index(request):
  mymembers = extendsPractice.objects.all().values()
  template = loader.get_template('template1.html')
  context = {
    'members': mymembers,
  }
  return HttpResponse(template.render(context, request))
from django.http import HttpResponse
from django.template import loader
from .models import extendsPractice


def index(request):
  mymembers = extendsPractice.objects.all().values()
  template = loader.get_template('index3.html')
  context = {
    'members': mymembers,
  }
  return HttpResponse(template.render(context, request))

