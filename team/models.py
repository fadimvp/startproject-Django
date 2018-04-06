from django.db import models

# Create your models here.

class SignUp(models.Model):
    email= models.EmailField()
    full_name=models.CharField(max_length=120,blank=True,null=True)
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
    update=models.DateTimeField(auto_now_add=False,auto_now=True)
    def __unicode__(self):
        return self.email

class Join (SignUp):


    ref_id =models.CharField(max_length=150,default='ABC')
    ip_address= models.CharField(max_length=120,default='ABC')
    def __unicode__(self):
        return self.ip_address

class Hour(Join):
    ph =models.CharField(max_length=120)
    def __unicode__(self):
        return self.ph