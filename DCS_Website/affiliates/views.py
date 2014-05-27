from django.shortcuts import render
from people.models import Affiliate

# Create your views here.
def affiliate(request):
    """Fetch the requested objects with the given primary keys from the database,
    create context by assigning the objects to corresponding variables in the template,
    and render the page using the context and the template in the given directory.
    """
    affiliate_list = Affiliate.objects.order_by('-name') 
    
    affiliate_context = {'affiliate_list' : affiliate_list,
  	}
    return render(request, 'affiliates/affiliates.html', affiliate_context)
