from django import forms
from django.forms import ValidationError
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

from accounts.models import CustomUser


class UserCacheMixin:
    user_cache = None


class SignIn(UserCacheMixin, forms.Form):
    password = forms.CharField(
        label=_("Password"), strip=False, widget=forms.PasswordInput
    )


class SignInViaUsernameForm(SignIn):
    username = forms.CharField(label=_("Username"))

    @property
    def field_order(self):
        return ["username", "password"]

    def clean_username(self):
        username = self.cleaned_data["username"]

        user = CustomUser.objects.filter(username=username).first()
        if not user:
            raise ValidationError(_("You entered an invalid username."))

        if not user.is_active:
            raise ValidationError(_("This account is not active."))

        self.user_cache = user

        return username


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = settings.SIGN_UP_FIELDS
