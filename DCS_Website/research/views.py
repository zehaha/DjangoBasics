from django.shortcuts import render
from research.models import Lab, Adviser, Field

# Create your views here.
def research(request):
    """Fetch the requested objects with the given primary keys from the database,
    create context by assigning the objects to corresponding variables in the template,
    and render the page using the context and the template in the given directory.
    """
    lab_list = Lab.objects.order_by('name')

    research_context = {'lab_list' : lab_list}
    return render(request, 'research/research.html', research_context)
	
	
	
