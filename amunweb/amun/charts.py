from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.db.models import Count, Sum

from amun.models import initial_connection, successful_exploit, successful_submission

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib as mpl
from pylab import axes

def top_shellcode(request):
	shellcode_list = successful_exploit.objects.values('shellcode_name').annotate(Count("count")).order_by('-count__count')[:10]
	shell = []
	counts = []
	explodes = []
	colors = ['#FFCCCC', '#FF9999', '#FF6666', '#FF3333', '#FF0000', '#CC0000', '#990000', '#660000', '#330000', '#000000']
	for item in shellcode_list:
		shell.append(item['shellcode_name'])
		counts.append(item['count__count'])
		if len(counts)>=10:
			break
	for value in xrange(0, len(counts)):
		explodes.append(0)
	if len(explodes)>0:
		explodes[0] = 0.1
	fig = Figure(figsize=(5, 3), dpi=80, facecolor='w', edgecolor='k')
	ax = fig.add_axes([0.25, 0.3, 0.5, 0.5])
	mpl.rcParams['font.size'] = 9.0
	pie_wedge_collection = ax.pie(counts, explode=explodes, labels=shell, autopct='%1.1f%%', shadow=True, startangle=180, radius=1.5, colors=colors)
	for pie_wedge in pie_wedge_collection[0]:
			pie_wedge.set_edgecolor('white')
	ax.axis('equal')
	canvas = FigureCanvas(fig)
	response = HttpResponse(content_type='image/png')
	canvas.print_png(response)
	return response

def top_attacker(request):
	connection_list = initial_connection.objects.values('attacker_ip').annotate(count=Sum("count")).order_by('-count')[:10]
	ips = []
	counts = []
	explodes = []
	colors = ['#FFCCCC', '#FF9999', '#FF6666', '#FF3333', '#FF0000', '#CC0000', '#990000', '#660000', '#330000', '#000000']
	for item in connection_list:
		ips.append(item['attacker_ip'])
		counts.append(item['count'])
		if len(counts)>=10:
			break
	for value in xrange(0, len(counts)):
		explodes.append(0)
	if len(explodes)>0:
		explodes[0] = 0.1
	fig = Figure(figsize=(5, 3), dpi=80, facecolor='w', edgecolor='k')
	ax = fig.add_axes([0.25, 0.3, 0.5, 0.5])
	mpl.rcParams['font.size'] = 9.0
	pie_wedge_collection = ax.pie(counts, explode=explodes, labels=ips, autopct='%1.1f%%', shadow=True, startangle=180, radius=1.5, colors=colors)
	for pie_wedge in pie_wedge_collection[0]:
			pie_wedge.set_edgecolor('white')
	ax.axis('equal')
	canvas = FigureCanvas(fig)
	response = HttpResponse(content_type='image/png')
	canvas.print_png(response)
	return response

def top_ports(request):
	connection_list = initial_connection.objects.values('victim_port').annotate(Count("count")).order_by('-count__count')[:10]
	ports = []
	counts = []
	explodes = []
	colors = ['#FFCCCC', '#FF9999', '#FF6666', '#FF3333', '#FF0000', '#CC0000', '#990000', '#660000', '#330000', '#000000']
	for item in connection_list:
		ports.append(item['victim_port'])
		counts.append(item['count__count'])
		if len(counts)>=10:
			break
	for value in xrange(0, len(counts)):
		explodes.append(0)
	if len(explodes)>0:
		explodes[0] = 0.1
	fig = Figure(figsize=(5, 3), dpi=80, facecolor='w', edgecolor='k')
	ax = fig.add_axes([0.25, 0.3, 0.5, 0.5])
	mpl.rcParams['font.size'] = 9.0
	pie_wedge_collection = ax.pie(counts, explode=explodes, labels=ports, autopct='%1.1f%%', shadow=True, startangle=180, radius=1.5, colors=colors)
	for pie_wedge in pie_wedge_collection[0]:
			pie_wedge.set_edgecolor('white')
	ax.axis('equal')
	canvas = FigureCanvas(fig)
	response = HttpResponse(content_type='image/png')
	canvas.print_png(response)
	return response

def top_vulns(request):
	exploit_list = successful_exploit.objects.values('vulnerability_name').annotate(Count("count")).order_by('-count__count')[:10]
	vulns = []
	counts = []
	explodes = []
	colors = ['#FFCCCC', '#FF9999', '#FF6666', '#FF3333', '#FF0000', '#CC0000', '#990000', '#660000', '#330000', '#000000']
	for item in exploit_list:
		vulns.append(item['vulnerability_name'])
		counts.append(item['count__count'])
		if len(counts)>=10:
			break
	for value in xrange(0, len(counts)):
		explodes.append(0)
	if len(explodes)>0:
		explodes[0] = 0.1
	fig = Figure(figsize=(5, 3), dpi=80, facecolor='w', edgecolor='k')
	ax = fig.add_axes([0.25, 0.3, 0.5, 0.5])
	mpl.rcParams['font.size'] = 9.0
	pie_wedge_collection = ax.pie(counts, explode=explodes, labels=vulns, autopct='%1.1f%%', shadow=True, startangle=180, radius=1.5, colors=colors)
	for pie_wedge in pie_wedge_collection[0]:
			pie_wedge.set_edgecolor('white')
	ax.axis('equal')
	canvas = FigureCanvas(fig)
	response = HttpResponse(content_type='image/png')
	canvas.print_png(response)
	return response

