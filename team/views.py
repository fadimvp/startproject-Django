from django.conf import settings
from django.core.mail import send_mail

from django.shortcuts import render

# Create your views here.
from team.forms import SignUpForm,ContectForm,JoinFrom,HourForm

from models import SignUp,Join


def home(request):
    print request.META.get("REMOTE_ADDR")
    print request.META.get("HTTP_X_FORWARDED_FOR")

    title=" Welcome"
    forms= SignUpForm(request.POST or None)
    context = {
        "tile": title,

    }
    if forms.is_valid():
       forms.save()




    if request.user.is_authenticated() and request.user.is_staff:

       queryset=SignUp.objects.all().order_by('-timestamp')


       # print SignUp.objects.all()
       #i=1
       #for instan in SignUp.objects.all():
           # print i
           # print instan
           # i+=1

       context={
           "froms": forms,
                "queryset":queryset,
            }
    return render(request,'home.html',context)





#------------------------------------
def shar(request):
    formss = HourForm(request.POST or None)
    if formss.is_valid():
        new_join=formss.save(commit=False)
        email=formss.cleaned_data['email']
        print email
        new_join.save()

    context ={
        'forms':formss
    }

    return render(request,'shar.html',context)

#----------------------------------------


def contect(request):
    title='Content Us'
    form=ContectForm(request.POST or None)
    if form.is_valid():
        #for key in form.cleaned_data:
           # print(form.cleaned_data.get(key))
     form_email=form.cleaned_data.get('email')
     form_full_name=form.cleaned_data.get('full_name')
     form_messge=form.cleaned_data.get('messge')
     subject='site contact form '
     from_email=settings.EMAIL_HOST_USER
     to_email=[from_email, 'yourgmail@gmail.com']
     contacct_messge=" %s: %s via %s"%(form_full_name,
                                        form_messge,
                                        form_email)
     send_mail(subject,
               contacct_messge,
               from_email,
               to_email
               ,fail_silently=True)

    context={

        'form': form,
        'title':title
    }
    return render(request,'forms.html',context)
def loginout (request):
    context={

    }
    return render(request,'loginout.html',context)
#------------------------------------------------
def hour(request):
    forms = HourForm(request.POST or None)
    if forms.is_valid():
        new_join=forms.save(commit=False)
        email=forms.cleaned_data['email']
        print email
        new_join.save()

    conte ={
        'forms':forms
    }
    template='hour.html'
    return render(request,template,conte)
