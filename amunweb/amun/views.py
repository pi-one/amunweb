from django.shortcuts import render_to_response, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from amun.forms import SearchForm
from amun.models import initial_connection, successful_exploit, successful_submission

# Create your views here.

def home(request):
	return render_to_response('amun/home.html')

def contact(request):
	return render_to_response('amun/contact.html')

def search(request):
	if request.method == 'POST':
		form = SearchForm(request.POST)
		if form.is_valid():
			term = form.cleaned_data['query']
			try:
				result = initial_connection.objects.all().filter(attacker_ip__icontains=term).order_by('-last_seen')
			except:
				result = None
		else:
			result = None
	else:
		form = SearchForm()
		result = None
	return render(request, 'amun/search.html', {'form': form, 'result': result})

def initial_details(request, connection_id):
	try:
		connection = initial_connection.objects.get(pk=connection_id)
	except initial_connection.DoesNotExist:
		connection = None
	if connection:
		try:
			exploits = successful_exploit.objects.all().filter(attacker__attacker_ip=connection.attacker_ip)
		except successful_exploit.DoesNotExist:
			exploits = None
		if exploits:
			try:
				submissions = successful_submission.objects.all().filter(exploit__attacker__attacker_ip=connection.attacker_ip)
			except successful_exploit.DoesNotExist:
				submissions = None
		else:
			submissions = None
	else:
		exploits = None
		submissions = None
	return render_to_response('amun/initial_details.html', {'connection': connection, 'exploits': exploits, 'submissions': submissions})

def exploit_details(request, exploit_id):
	try:
		exploit = successful_exploit.objects.get(pk=exploit_id)
	except successful_exploit.DoesNotExist:
		exploit = None
	if exploit:
		try:
			submissions = successful_submission.objects.all().filter(exploit__attacker__attacker_ip=exploit.attacker.attacker_ip)
		except successful_exploit.DoesNotExist:
			submissions = None
	else:
		submissions = None
	return render_to_response('amun/exploit_details.html', {'exploit': exploit, 'submissions': submissions})

def submission_details(request, submission_id):
	try:
		submission = successful_submission.objects.get(pk=submission_id)
	except successful_submission.DoesNotExist:
		submission = None
	if submission:
		try:
			exploits = successful_exploit.objects.all().filter(attacker__attacker_ip=submission.exploit.attacker.attacker_ip)
		except successful_exploit.DoesNotExist:
			exploits = None
	else:
		exploits = None
	return render_to_response('amun/submission_details.html', {'submission': submission, 'exploits': exploits})

def submissions(request):
	submissions_list = successful_submission.objects.select_related().order_by('-last_seen')
	paginator = Paginator(submissions_list, 20)
	page = request.GET.get('page')
	try:
		submissions = paginator.page(page)
	except PageNotAnInteger:
		submissions = paginator.page(1)
	except EmptyPage:
		submissions = paginator.page(paginator.num_pages)
	return render_to_response('amun/submissions.html', {'submissions': submissions})

def exploits(request):
	exploits_list = successful_exploit.objects.select_related().order_by('-last_seen')
	paginator = Paginator(exploits_list, 20)
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
	paginator = Paginator(connects_list, 20)
	page = request.GET.get('page')
	try:
		connects = paginator.page(page)
	except PageNotAnInteger:
		connects = paginator.page(1)
	except EmptyPage:
		connects = paginator.page(paginator.num_pages)
	return render_to_response('amun/initials.html', {'connects': connects})
