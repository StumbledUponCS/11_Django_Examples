from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import QueryTest


def index(request):
    mymembers = QueryTest.objects.all().values()
    template = loader.get_template('index.html')
    context = {
    'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))


def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))


def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    member = QueryTest(firstname=x, lastname=y)
    member.save()
    return HttpResponseRedirect(reverse('index'))


def delete(request, id):
    member = QueryTest.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))


def update(request, id):
    mymember = QueryTest.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
     'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))


def updaterecord(request, id):
    first = request.POST['first']
    last = request.POST['last']
    member = QueryTest.objects.get(id=id)
    member.firstname = first
    member.lastname = last
    member.save()
    return HttpResponseRedirect(reverse('index'))





#
#
#def testing(request):
#  mymembers = QueryTest.objects.all().values()
#  template = loader.get_template('template.html')
#  context = {
#    'mymembers': mymembers,
#  }
#  return HttpResponse(template.render(context, request))
#


# def testing(request):
#   template = loader.get_template('template.html')
#   context = {
#     'firstname': 'Linus',
#   }
#   return HttpResponse(template.render(context, request))












  
#def index(request):
#  mymembers = ResumeInput.objects.all().values()
#  template = loader.get_template('index.html')
#  context = {
#    'mymembers': mymembers,
#  }
#  return HttpResponse(template.render(context, request))




#def index(request):
#  mymembers = ResumeInput.objects.all().values()
#  output = ""
#  for x in mymembers:
#    output += x["firstname"]
#  return HttpResponse(output)



#def index(request):
#    template = loader.get_template('myfirst.html')
#    return HttpResponse(template.render())



#def index(request):
#    return HttpResponse("Hello world!")

# Create your views here.

