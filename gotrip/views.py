from django.shortcuts import render, get_object_or_404
from .models import City
from .models import Festa
from .models import Insta

# Create your views here.
def home(request):
    citys = City.objects
    return render(request,'home.html', {'citys' : citys})

def example(request):
    citys = City.objects
    return render(request,'example.html', {'citys' : citys})

def generic(request, city_name):
    festas = Festa.objects.filter(tag = city_name)
    #festas = get_object_or_404(Festa, tag = city_name)
    return render(request, 'generic.html', {'festas': festas})

def gallery(request, festa_id):
    festa_detail = get_object_or_404(Festa, pk = festa_id)
    instas = Insta.objects.filter(tag = festa_detail.id)
    result1 = [];
    result2 = [];
    result3 = [];
    
    for i in range(0,3) :
        result1.append(instas[i]);

    for i in range(3,6) :
        result2.append(instas[i]);

    for i in range(6,9) :
        result3.append(instas[i]);
    
    return render(request, 'gallery.html', {'festa': festa_detail , 'instas1' : result1, 'instas2' : result2, 'instas3' : result3})
