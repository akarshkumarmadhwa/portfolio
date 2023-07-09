from django import forms
from django.contrib.auth.models import User
from django_secure_password_input.fields import DjangoSecurePasswordInput
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm, UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={"class": "form-control", "name": "username"}))
    password = DjangoSecurePasswordInput(
        label="Password",
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "name": "password",
                "type": "password"}))
    # captcha = CaptchaField(required=False)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.client_ip = self.get_client_ip(self.request)
        # LoginAttempts.list_records(self.client_ip)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
        return ip

    @property
    def is_show_captcha(self):
        return False

    @property
    def retry_count(self):
        pass
        # return LoginAttempts.retry_count(self.client_ip)

    def clean_captcha(self):
        captcha = self.data.get(u"captcha_1")
        if self.is_show_captcha and not captcha:
            raise forms.ValidationError("Please eneter correct captcha")
        return captcha

    def is_valid(self, *args, **kwargs):
        isvalid = super(LoginForm, self).is_valid(*args, **kwargs)
        if self.request.method == "POST":
            if isvalid:
                self.request.session['logged_ip'] = self.get_client_ip(self.request)
                self.request.session['logged_browser'] = self.request.META['HTTP_USER_AGENT']
                # LoginAttempts.remove_records(self.client_ip)
            # else:
                # LoginAttempts.record_failed(self.client_ip)
        return isvalid

