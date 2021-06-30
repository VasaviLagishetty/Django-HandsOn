from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
from django.apps import apps

# Create your views here.
def root(request):
    print("hello world")
    #m1 = Movie(1, 'gopala gopala', 'kishore')
    #m2 = Movie(2, 'Julayi', 'Trivikram')
    #l = [m1,m2]
    l = Movie.objects.filter(id = 2)
    print(l)
    return render(request,'page.html',{"movie":l})

def fun(request,display_name=''):
    print("display name",display_name)
    return render(request,'page.html',{"name":display_name})

def fun1(request,type=''):
    model_type = apps.get_model('sample',type)
    details = model_type.objects.all()
    return render(request, 'page.html', {"movie":details,"type":type})