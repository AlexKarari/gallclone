from django.shortcuts import render
from .models import Image, Category, Location
from django.http import Http404

# Create your views here.
def index(request):
    image = Image.objects.all()

    return render(request, 'all-pics/index.html', {"image": image})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Category.search_by_image_category(search_term)
        images = Image.get_Image_by_category(searched_images)
        message = f"{search_term}"

        return render(request, 'all-pics/search.html', {"message": message, "images": images})

    else:
        message = "You are yet to search for something."
        return render(request, 'all-news/search.html', {"message": message})

def location(request, location_id):
    try:
        location = Location.objects.get(id=location_id)
    except DoesNotExist:
        raise Http404()
    return render(request, "all-pics/location.html", {"location": location})
