from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.views.generic import View, FormView
from django.conf import settings


from .forms import SignInViaUsernameForm, SignUpForm


class GuestOnlyView(View):
    def dispatch(self, request, *args, **kwargs):
        # Redirect to the index page if the user already authenticated
        if request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)

        return super().dispatch(request, *args, **kwargs)


class LogInView(GuestOnlyView, FormView):
    template_name = "accounts/log_in.html"

    @staticmethod
    def get_form_class(**kwargs):
        return SignInViaUsernameForm

    def form_valid(self, form):
        request = self.request
        login(request, form.user_cache)
        return redirect("/")

    def post_login(sender, user, request, response, **kwargs):
        response.set_cookie("uid", user.uuid)
        return response


class SignUpView(GuestOnlyView, FormView):
    template_name = "accounts/sign_up.html"
    form_class = SignUpForm

    def form_valid(self, form):
        request = self.request
        user = form.save(commit=False)
        user.username = form.cleaned_data["username"]
        user.is_active = True
        user.save()
        raw_password = form.cleaned_data["password1"]
        user = authenticate(username=user.username, password=raw_password)
        login(request, user)
        messages.success(request, _("You are successfully signed up!"))
        return redirect("index")


class LogOutView(LoginRequiredMixin, BaseLogoutView):
    template_name = "accounts/log_out.html"
