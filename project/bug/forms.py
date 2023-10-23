from django import forms
from .models import Bug

class BugRegistrationForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ['description', 'bug_type', 'report_date', 'status']

        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'bug_type': forms.Select(attrs={'class': 'form-control'}),
            'report_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        } 
    
#def clean(self):

#        super(BugRegistrationForm, self).clean()
 #       description = self.cleaned_data.get('description')
#        if len(description) == 0 :
 #           self.errors['description'] = self.error_class(['This field is required'])
#
 #       return self.cleaned_data