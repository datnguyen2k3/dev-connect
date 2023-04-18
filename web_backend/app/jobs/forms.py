from django import forms
from .models.AppliedCV import AppliedCV

class AppliedCVForm(forms.ModelForm):
    class Meta:
        model = AppliedCV
        fields = ('cv_file', 'intro')
        
    def __init__(self, *args, **kwargs):
        super(AppliedCVForm, self).__init__(*args, **kwargs)

        for name_field, field in self.fields.items():
            field.widget.attrs.update({'class': 'input', 'placeholder': f'Add {name_field}'})

            # self.fields['title'].widget.attrs.update({'class': 'input'})

    