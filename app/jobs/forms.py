from django import forms
from .models.AppliedCV import AppliedCV

class AppliedCVForm(forms.ModelForm):
    class Meta:
        model = AppliedCV
        fields = ('cv_file', 'intro')

    