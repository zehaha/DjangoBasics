from django.shortcuts import render
from affiliates.models import Affiliate

# Create your views here.

def contact(request):
    return render(request, 'contact/contact.html')

def affiliates(request):
    affiliate_list = Affiliate.objects.all()
    return render(request, 'affiliates/affiliates.html', {'affiliate_list': affiliate_list,})

def about(request):
    gallery_images = Image.objects.order_by('-id').filter(models.Q(shown_in='g') | models.Q(shown_in='b'))[:6]
    context = {'gallery_images' : gallery_images,
                }
    return render(request, 'about/about.html', context)
