from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

def no_help_text(FormClass):
    base_init = FormClass.__init__

    def __init__(self, *args, **kwargs):
        base_init(self, *args, **kwargs)
        super(FormClass, self).__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.help_text = None

    FormClass.__init__ = __init__
    return FormClass

def add_placeholders(FormClass):
    base_init = FormClass.__init__

    def __init__(self, *args, **kwargs):
        base_init(self, *args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['placeholder'] = field.label

    FormClass.__init__ = __init__
    return FormClass

@add_placeholders
class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']

@add_placeholders
@no_help_text
class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
