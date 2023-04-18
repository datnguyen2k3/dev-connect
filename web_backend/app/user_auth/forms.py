from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        labels = {
            'username': 'Username',
        }

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].label = 'First Name'
        self.fields['last_name'].label = 'Last Name'
        self.fields['email'].label = 'Email'
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Confirm Password'

        for fieldname, field in self.fields.items():
            field.widget.attrs.update({'class': 'input', 'placeholder': f'Enter {field.label}'})
