from django.urls import path
from . import views





urlpatterns = [
   path('', views.index, name='index'),
   path('add/', views.add, name='add'),
   path('add/addrecord/', views.addrecord, name='addrecord'),
   path('delete/<int:id>', views.delete, name='delete'),
   path('update/<int:id>', views.update, name='update'),
   path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
]




#urlpatterns = [
#  path('', views.index, name='index'),
#  path('add/', views.add, name='add'),
#  path('add/addrecord/', views.addrecord, name='addrecord'),
#  path('delete/<int:id>', views.delete, name='delete'),
#  path('update/<int:id>', views.update, name='update'),
#]



#urlpatterns = [
#  path('', views.index, name='index'),
#  path('add/', views.add, name='add'),
#  path('add/addrecord/', views.addrecord, name='addrecord'),
#  path('delete/<int:id>', views.delete, name='delete'),
#]



#urlpatterns = [
#  path('', views.index, name='index'),
#  path('add/', views.add, name='add'),
#  path('add/addrecord/', views.addrecord, name='addrecord'),
#]



#urlpatterns = [
#  path('', views.index, name='index'),
#  path('add/', views.add, name='add'),
#]


#
#urlpatterns = [
#    path('', views.index, name='index'),
#]
