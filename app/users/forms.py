from app.users.models import Profile, Skill
from django import forms


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'location', 'email', 'short_intro', 'bio', 'profile_img',
                  'social_github', 'social_twitter', 'social_linkedin', 'social_youtube', 'social_website']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({'class': 'input', 'placeholder': f'Enter {field.label}'})


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'description']

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)

        for fieldname, field in self.fields.items():
            field.widget.attrs.update({'class': 'input', 'placeholder': f'Enter {field.label}'})
