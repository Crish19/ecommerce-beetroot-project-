from django import forms
from django.urls import reverse_lazy
from crispy_forms.helper import formerHelper 
from crispy_forms.helper import Submit 

class UserLoginForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = formerHelper(self)
        self.helper.form_action = reverse_lazy('index')
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Submit'))

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Username', 'id': 'login-username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'id': 'login-pwd',
        }
    ))

# class RegistrationForm(forms.ModelForm):

#     user_name = forms.CharField(
#         label='Enter Username', min_length=4, max_length=50, help_text='Required')
#     email = forms.EmailField(max_length=100, help_text='Required', error_messages={
#         'required': 'Sorry, you will need an email'})
#     password = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(
#         label='Repeat password', widget=forms.PasswordInput)

#     class Meta:
#         model = UserBase
#         fields = ('user_name', 'email',)
     