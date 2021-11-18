from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Lostitems

# Create your views here.

def base(request):
    
    all_items = Lostitems.objects.all().order_by('-date')
    
    context = {"all_items":all_items}
    
    return render(request, 'main/base.html', context)

def home(request, item_id):
    
    items = get_object_or_404(Lostitems, pk=item_id)
    
    context = {'items':items}

    return render(request, 'main/home.html', context)

def search(request):
    
    all_items = Lostitems.objects.all().order_by('-date')

    if len(request.GET) == 0:
        relevant_items = all_items
    else:
        search_string = request.GET['q']
        relevant_items = all_items.filter(name__contains = search_string)
    
    context = {'relevant_items':relevant_items}

    return render(request, 'main/search.html', context)
