from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User

# Our form is based on the form provided by Django
class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        # making 'email' field required
        self.fields['email'].required = True

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'username',  
                'password1', 'password2']
        