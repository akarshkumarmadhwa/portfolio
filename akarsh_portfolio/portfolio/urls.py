from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from portfolio.forms import LoginForm
from portfolio.views import portfolio, resiterPage

urlpatterns = [
    path("",LoginView.as_view(
        template_name="login.html",
        authentication_form=LoginForm
    ),
    name="login"),
    path("register/",resiterPage,
    name="register"),
    path("portfolio/",portfolio,name="portfolio")
]