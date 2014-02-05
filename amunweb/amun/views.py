from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from amun.models import initial_connection, successful_exploit, successful_submission

# Create your views here.

def home(request):
	return render_to_response('amun/home.html')

def contact(request):
	return render_to_response('amun/contact.html')

def initial_details(request, connection_id):
	try:
		connection = initial_connection.objects.get(pk=connection_id)
	except initial_connection.DoesNotExist:
		connection = None
	return render_to_response('amun/initial_details.html', {'connection': connection})

def exploit_details(request, exploit_id):
	try:
		exploit = successful_exploit.objects.get(pk=exploit_id)
	except successful_exploit.DoesNotExist:
		exploit = None
	print exploit
	return render_to_response('amun/exploit_details.html', {'exploit': exploit})

def submissions(request):
	submissions_list = successful_submission.objects.select_related().order_by('-last_seen')
	paginator = Paginator(submissions_list, 25)
	page = request.GET.get('page')
	try:
		submissios = paginator.page(page)
	except PageNotAnInteger:
		submissions = paginator.page(1)
	except EmptyPage:
		submissions = paginator.page(paginator.num_pages)
	return render_to_response('amun/submissions.html', {'submissions': submissions})

def exploits(request):
	exploits_list = successful_exploit.objects.select_related().order_by('-last_seen')
	paginator = Paginator(exploits_list, 25)
	page = request.GET.get('page')
	try:
		exploits = paginator.page(page)
	except PageNotAnInteger:
		exploits = paginator.page(1)
	except EmptyPage:
		exploits = paginator.page(paginator.num_pages)
	return render_to_response('amun/exploits.html', {'exploits': exploits})

def initials(request):
	connects_list = initial_connection.objects.order_by('-last_seen')
	paginator = Paginator(connects_list, 25)
	page = request.GET.get('page')
	try:
		connects = paginator.page(page)
	except PageNotAnInteger:
		connects = paginator.page(1)
	except EmptyPage:
		connects = paginator.page(paginator.num_pages)
	return render_to_response('amun/initials.html', {'connects': connects})
