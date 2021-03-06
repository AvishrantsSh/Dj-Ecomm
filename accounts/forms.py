from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserChangeForm,
    UserCreationForm,
)

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label="Name",
        widget=forms.TextInput(
            attrs={
                "required": "True",
                "class": "text-box",
                "autocomplete": "name",
            }
        ),
    )
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "required": "True",
                "class": "text-box",
                "autocomplete": "phone",
            }
        )
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "required": "True",
                "class": "text-box",
                "autocomplete": "email",
            }
        )
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "required": "True",
                "class": "text-box",
                "autocomplete": "new-password",
            }
        ),
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={
                "required": "True",
                "class": "text-box",
                "autocomplete": "new-password",
            }
        ),
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("username", "email", "phone", "password1", "password2")


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget = forms.EmailInput()
        self.fields["username"].widget.attrs.update(
            {
                "required": "True",
                "class": "text-box",
                "autocomplete": "username",
                "id": "email",
            }
        )
        self.fields["password"].widget.attrs.update(
            {
                "required": "True",
                "class": "text-box",
                "autocomplete": "password",
            }
        )

    class Meta:
        model = CustomUser
        fields = ("email", "password")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
