from django.http import HttpResponse
from django.template import loader
from .models import querySetPrac
from django.db.models import Q





#Multiple Order Bys:
#
#
#To order by more than one field, separate the fieldnames with a comma in the order_by() method:
#
#
#Example :
#
#Order the the result first by lastname ascending, then descending on id:


def index(request):
  mydata = querySetPrac.objects.all().order_by('lastname', '-id').values()
  template = loader.get_template('index6.html')
  context = {
    'members': mydata,
  }
  return HttpResponse(template.render(context, request))
  








#Descending Order:
#
#
#By default, the result is sorted ascending (the lowest value first), to change the direction to descending (the highest value first), use the minus sign (NOT), - in front of the field name:
#
#
#Example:
#
#Order the the result firstname descending:




#def index(request):
#  mydata = querySetPrac.objects.all().order_by('-firstname').values()
#  template = loader.get_template('index6.html')
#  context = {
#    'members': mydata,
#  }
#  return HttpResponse(template.render(context, request))
#  


#
#Order By:


#To sort QuerySets, Django uses the order_by() method:
#

#Example:

#Order the the result alphabetically by firstname:


#def index(request):
#  mydata = querySetPrac.objects.all().order_by('firstname').values()
#  template = loader.get_template('index6.html')
#  context = {
#    'members': mydata,
#  }
#  return HttpResponse(template.render(context, request))
#


#Field Lookups Syntax :
#
#All Field lookup keywords must be specified with the fieldname, followed by two(!) underscore characters, and the keyword.
#
#In our Members model, the statement would be written like this:

#
#def index(request):
#  mydata = querySetPrac.objects.filter(firstname__startswith='L').values()
#  template = loader.get_template('index6.html')
#  context = {
#    'members': mydata,
#  }
#  return HttpResponse(template.render(context, request))
#


#Another common method is to import and use Q expressions:
#
#Example


#Return records where firstname is either "Emil" or Tobias":
#
#


#def index(request):
#  mydata = querySetPrac.objects.filter(Q(firstname='Emil') | Q(firstname='Tobias')).values()
#  template = loader.get_template('index6.html')
#  context = {
#    'members': mydata,
#  }
#  return HttpResponse(template.render(context, request))
#
#
#



#OR :
#
#
#To return records where firstname is Emil or firstname is Tobias (meaning: returning records that matches either query, not necessarily both) is not as easy as the AND example above.
#
#We can use multiple filter() methods, separated by a pipe | character. The results will merge into one model.


#def index(request):
#  mydata = querySetPrac.objects.filter(firstname='Emil').values() | querySetPrac.objects.filter(firstname='Tobias').values()
#  template = loader.get_template('index6.html')
#  context = {
#    'members': mydata,
#  }
#  return HttpResponse(template.render(context, request))
#





#
#AND :
#
#
#The filter() method takes the arguments as **kwargs (keyword arguments), so you can filter on more than one field by sepearting them by a comma.
#



#def index(request):
#  mydata = querySetPrac.objects.filter(lastname='Refsnes', id=12).values()
#  template = loader.get_template('index6.html')
#  context = {
#    'members': mydata,
#  }
#  return HttpResponse(template.render(context, request))




#Return Specific Rows :
#
#
#You can filter the search to only return specific rows/records, by using the filter() method.

#def index(request):
#  mydata = querySetPrac.objects.filter(firstname='Emil').values()
#  template = loader.get_template('index6.html')
#  context = {
#    'members': mydata,
#  }
#  return HttpResponse(template.render(context, request))
#


# Check out template.html to see how the mymembers object
# was used in the HTML code.



#Return Specific Columns :


#The values_list() method allows you to return only the columns that you specify.

#def index(request):
#  mydata = querySetPrac.objects.values_list('firstname')
#  template = loader.get_template('index7.html')
#  context = {
#    'members': mydata,
#  }
#  return HttpResponse(template.render(context, request))
#




#The values() Method :


#The values() method allows you to return each object as a Python dictionary, with the names and values as key/value pairs:


#def index(request):
#  mymembers = querySetPrac.objects.all().values()
#  template = loader.get_template('index6.html')
#  context = {
#    'members': mymembers,
#  }
#  return HttpResponse(template.render(context, request))
#
