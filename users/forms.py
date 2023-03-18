from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.models import Profile, Skill
from django import forms

class CustomUserCreationFrom(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        labels = {
            'username': 'Username',
        }
        
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationFrom, self).__init__(*args, **kwargs)
        
        self.fields['first_name'].label = 'First Name'
        self.fields['last_name'].label = 'Last Name'
        self.fields['email'].label = 'Email'
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Confirm Password'
        
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({'class': 'input', 'placeholder': f'Enter {field.label}'})
            
            
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
        
