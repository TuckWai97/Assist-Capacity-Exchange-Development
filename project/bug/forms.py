from django import forms
from .models import Bug

class BugRegistrationForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ['description', 'bug_type', 'report_date', 'status']

        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control','placeholder':'Text description for the bug'}),
            'bug_type': forms.Select(attrs={'class': 'form-control'}),
            'report_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        } 
