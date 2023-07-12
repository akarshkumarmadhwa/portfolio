from django.conf import settings
from django.shortcuts import redirect, render

from portfolio.forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

login_url = settings.LOGIN_URL


def resiterPage(request):
    form = CustomUserCreationForm
    if request.method == "POST":
        form =  CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        
    context = {"form":form}
    return render(request, "register.html", context)

@login_required(login_url=login_url)
def portfolio(request):
    return render(request,"index.html")

def LogoutView(request):
    pass
