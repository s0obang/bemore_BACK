from django import forms
from .models import Applicant

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ['name', 'phone_number', 'introduction', 'motivation', 'activity_attachment', 'github_or_tistory']
        