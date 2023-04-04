from django.forms import ModelForm
from .models.Project import Project
from django import forms


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'featured_img',
                  'demo_link', 'source_link', 'skill_tags']

        widgets = {
            'skill_tags': forms.CheckboxSelectMultiple()
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for name_field, field in self.fields.items():
            field.widget.attrs.update({'class': 'input', 'placeholder': f'Add {name_field}'})

            # self.fields['title'].widget.attrs.update({'class': 'input'})
