from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from .models import Image,Category,Location

# Create your views here.
def landing(request):
    date = dt.date.today()
    images = Image.objects.all()
    return render (request,'landing.html',{"date":date,"images":images})

def gallery(request):
    images_item= Image.objects.all()
    return render(request,'pictures.html',{"images":images_item})

def search_results(request):

    if 'images' in request.GET and request.GET["images"]:
        search_term = request.GET.get("images")
        searched_images= Category.search_by_category(search_term)
        searched_images= Location.search_by_location(search_term)
        message = f"{search_term}"
        images_item=Image.objects.all()

        return render(request, 'search.html',{"message":message,"images": searched_images,"images":images_item})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
