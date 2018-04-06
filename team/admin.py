from django.contrib import admin
from django.contrib.sites.models import RequestSite
# Register your models here.
from .forms import SignUpForm ,ContectForm,JoinFrom
from .models import SignUp,Join,Hour
class SignUpAdmin(admin.ModelAdmin):
    list_display = ['email','full_name','update']
    form = SignUpForm


    #class Meta:
       # model =SignUp
class JoinupAdmin(admin.ModelAdmin):
    list_display = ['email','ref_id','ip_address','update','full_name']
    form = JoinFrom
class HourAdmin(admin.ModelAdmin):
    list_display = ['ph',"full_name"]
    form = JoinFrom
admin.site.register(Join,JoinupAdmin)
admin.site.register(SignUp,SignUpAdmin)
admin.site.register(Hour,HourAdmin)

