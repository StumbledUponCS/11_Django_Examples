from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import TemplatePrac



def testing(request):
  mymembers_o = TemplatePrac.objects.all().values()
  template = loader.get_template('index2.html')
  context = {
    'firstname': 'Linus',
    'mymembers': mymembers_o,
    'greeting': 4,
    'day': "Friday",
    'x': ['Apple', 'Banana', 'Cherry'], 
    'y': ['Apple', 'Banana', 'Cherry'], 
    'fruits': ['Apple', 'Banana', 'Cherry'], 
    'fruits2': ['Apple', 'Kiwi', 'Cherry']
  }
  return HttpResponse(template.render(context, request))



# def testing(request):
#   template = loader.get_template('template.html')
#   context = {
#     'firstname': 'Linus',
#   }
#   return HttpResponse(template.render(context, request))




# def index(request):
#   mymembers = TemplatePrac.objects.all().values()
#   output = ""
#   for x in mymembers:
#     output += x["fname"]
#   return HttpResponse(output)



#def index(request):
#  template = loader.get_template('myfirst.html')
#  return HttpResponse(template.render())
