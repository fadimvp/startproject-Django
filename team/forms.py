from  django import forms
from .models import SignUp,Join,Hour

class ContectForm(forms.Form):
    full_name=forms.CharField(max_length=150)
    email=forms.EmailField()
    messge=forms.CharField(max_length=256)
class SignUpForm(forms.ModelForm):
    class Meta:
        model=SignUp
        fields=['email','full_name']
    def clean_email(self):
        email=self.cleaned_data.get('email')
        if not 'gmail' in email:
            raise forms.ValidationError("pleas enter gmail.com")
        return email
    def clean_full_name(self):
        full_name=self.cleaned_data.get("full_name")
        return full_name
class JoinFrom(forms.ModelForm):
    class Meta:
        model = Join

        fields = ['full_name','email','ip_address','ref_id']
class HourForm(SignUpForm,JoinFrom):
    class Meta:
        model= Hour
        fields = ['full_name','ph','email','ip_address']




