from django import forms
from .models import Job

#Create Job Form
class CreateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('user', 'company')

#Update Job Form
class UpdateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('user', 'company')