from django.shortcuts import render
from affiliates.models import Affiliate

# Create your views here.
def affiliates(request):
    affiliate_list = Affiliate.objects.all()
    return render(request, 'affiliates/affiliates.html', {'affiliate_list': affiliate_list,})
