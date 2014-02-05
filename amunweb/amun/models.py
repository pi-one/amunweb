from django.db import models

class initial_connection(models.Model):
	attacker_ip = models.IPAddressField()
	attacker_port = models.PositiveIntegerField()
	victim_ip = models.IPAddressField()
	victim_port = models.PositiveIntegerField()
	count = models.PositiveIntegerField(default=1)
	first_seen = models.DateTimeField(null=True, auto_now=False, auto_now_add=True)
	last_seen = models.DateTimeField(null=True, auto_now=True, auto_now_add=False)
	sensor_id = models.PositiveIntegerField()

	class Meta:
		unique_together = ('attacker_ip', 'victim_ip', 'victim_port', 'sensor_id')
		index_together = [
					["attacker_ip", "victim_ip", "victim_port", "sensor_id"]
				]
		get_latest_by = 'last_seen'

class successful_exploit(models.Model):
	attacker = models.ForeignKey(initial_connection)
	vulnerability_name = models.CharField(max_length=256, blank=True, db_index=True)
	download_method = models.CharField(max_length=256, blank=True)
	shellcode_name = models.CharField(max_length=256, blank=True)
	count = models.PositiveIntegerField(default=1)
	first_seen = models.DateTimeField(auto_now=False, auto_now_add=True)
	last_seen = models.DateTimeField(auto_now=True, auto_now_add=False)

	class Meta:
		index_together = [
					["vulnerability_name", "download_method", "shellcode_name"]
				]
		get_latest_by = 'last_seen'

class successful_submission(models.Model):
	exploit = models.ForeignKey(successful_exploit)
	download_url = models.CharField(max_length=1025)
	md5_hash = models.CharField(max_length=32)
	sha256_hash = models.CharField(max_length=64)
	count = models.PositiveIntegerField(default=1)
	first_seen = models.DateTimeField(auto_now=False, auto_now_add=True)
	last_seen = models.DateTimeField(auto_now=True, auto_now_add=False)

	class Meta:
		unique_together = ('download_url', 'md5_hash', 'sha256_hash')
		index_together = [
					["download_url", "md5_hash", "sha256_hash"]
				]
		get_latest_by = 'last_seen'
