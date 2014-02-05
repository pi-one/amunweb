from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'amun.views.home', name='home'),
	url(r'^initials$', 'amun.views.initials', name='initials'),
	url(r'^initial/(?P<connection_id>\d{1,})/details$', 'amun.views.initial_details', name='initial_details'),
	url(r'^exploits$', 'amun.views.exploits', name='exploits'),
	url(r'^exploit/(?P<exploit_id>\d{1,})/details$', 'amun.views.exploit_details', name='exploit_details'),
	url(r'^submissions$', 'amun.views.submissions', name='submissions'),
	url(r'^submission/(?P<submission_id>\d{1,})/details$', 'amun.views.submission_details', name='submission_details'),
	url(r'^contact$', 'amun.views.contact', name='contact'),
	url(r'^charts/top_ports.png$', 'amun.charts.top_ports', name='top_ports'),
	url(r'^charts/top_vulns.png$', 'amun.charts.top_vulns', name='top_vulns'),
	url(r'^charts/top_attacker.png$', 'amun.charts.top_attacker', name='top_attacker'),
	url(r'^charts/top_shellcode.png$', 'amun.charts.top_shellcode', name='top_shellcode'),
)
