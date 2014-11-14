from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from accounts.models import UserProfile

@login_required
def add_request(request):
	context = RequestContext(request)

	return render_to_response('home/request_form.html', context)

@login_required
def request_detail(request):
	context = RequestContext(request)

	return render_to_response('home/request_details.html', context)

@login_required
def reservation_list(request):
	context = RequestContext(request)

	return render_to_response('home/reservation_lists.html', context)