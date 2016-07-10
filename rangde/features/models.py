from __future__ import unicode_literals

from django.db import models

class investor_info_table(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    mobile_number = models.IntegerField(null=True, blank=True)
    email_id = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "investor_info"
        
class seek_info_table(models.Model):
    visitor_name = models.CharField(max_length=255, null=True, blank=True)
    refer_name = models.CharField(max_length=255, null=True, blank=True)
    mobile_number = models.CharField(max_length=255, null=True, blank=True)
    email_id = models.CharField(max_length=255, null=True, blank=True)
    
    class Meta:
        db_table = "seek_info"
        
class refer_info_table(models.Model):
    referrer_name = models.CharField(max_length=255, null=True, blank=True)
    referred_name = models.CharField(max_length=255, null=True, blank=True)
    email_id = models.CharField(max_length=255, null=True, blank=True)
    mobile_number = models.CharField(max_length=255,null=True, blank=True)
            

    class Meta:
        db_table = "refer_info"
