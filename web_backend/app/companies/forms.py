from django import forms
from .models.CompanyReview import CompanyReview

class CompanyReviewForm(forms.ModelForm):
    class Meta:
        model = CompanyReview
        fields = ['title', 'advantage', 'defect', 'salary_stars', 'training_stars', 'employee_attention_stars', 'culture_stars', 'office_starts']
        
    def __init__(self, *args, **kwargs):
        super(CompanyReviewForm, self).__init__(*args, **kwargs)

        for name_field, field in self.fields.items():
            field.widget.attrs.update({'class': 'input', 'placeholder': f'Add {name_field}'})

            # self.fields['title'].widget.attrs.update({'class': 'input'})

    