from django.shortcuts import render
from django.db import models
from images.models import Image


# Create your views here.
def about(request):
    gallery_images = Image.objects.order_by('-id').filter(models.Q(shown_in='g') | models.Q(shown_in='b'))[:6]
    context = {'gallery_images' : gallery_images,
                }
    return render(request, 'about/about.html', context)
