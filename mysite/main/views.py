from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Lostitems

# Create your views here.

def index(request):
    
    all_items = Lostitems.objects.all().order_by('-date')
    context = {"all_items":all_items}
    return render(request, 'main/base.html', context)

def home(request, item_id):
    
    item = get_object_or_404(Lostitems, pk=item_id)
    context = {'item':item}

    return render(request, 'main/home.html', context)