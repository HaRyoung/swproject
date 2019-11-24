from django.shortcuts import render, get_object_or_404
from .models import City
from .models import Festa

# Create your views here.
def home(request):
    citys = City.objects
    return render(request,'home.html', {'citys' : citys})

def example(request):
    citys = City.objects
    return render(request,'example.html', {'citys' : citys})

def generic(request, city_name):
    print(city_name)
    festas = Festa.objects.filter(tag = city_name)
    #festas = get_object_or_404(Festa, tag = city_name)
    return render(request, 'generic.html', {'festas': festas})
