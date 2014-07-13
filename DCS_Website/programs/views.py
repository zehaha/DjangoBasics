from django.shortcuts import render
from django.templatetags.static import static
from django.core.servers.basehttp import FileWrapper

# Create your views here.
def programs(request):
    return render(request, 'programs/programs.html')
