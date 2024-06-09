from django.db import models

# Create your models here.
class logindb(models.Model):
    s_name = models.CharField(max_length=100, null=True, blank=True)
    s_mail = models.CharField(max_length=100, null=True, blank=True)
    s_pass = models.CharField(max_length=100, null=True, blank=True)

class senderdb(models.Model):
    se_f_name = models.CharField(max_length=100, null=True, blank=True)
    se_mobile = models.CharField(max_length=100, null=True, blank=True)
    se_address = models.CharField(max_length=100, null=True,blank=True)


class receiverdb(models.Model):
    email = models.CharField(max_length=100, null=True, blank=True)
    re_f_name = models.CharField(max_length=100, null=True, blank=True)
    re_mobile = models.CharField(max_length=100, null=True, blank=True)
    re_address = models.CharField(max_length=100, null=True,blank=True)
    re_date = models.DateField(null=True, default='', blank=True)
    re_status = models.CharField(max_length=100, null=True, blank=True)


class prodb(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.CharField(max_length=100, null=True, blank=True)
    address_1 = models.CharField(max_length=100, null=True, blank=True)
    address_2 = models.CharField(max_length=100, null=True, blank=True)
    post_code = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    area = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    # email = models.CharField(max_length=100, null=True, blank=True)
    # password = models.CharField(max_length=100, null=True, blank=True)

class contactdb(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    subject = models.CharField(max_length=100, null=True, blank=True)
    message = models.CharField(max_length=200, null=True, blank=True)
