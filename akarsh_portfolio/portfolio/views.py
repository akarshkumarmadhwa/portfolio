from django.shortcuts import redirect, render

from portfolio.forms import CustomUserCreationForm


def resiterPage(request):
    form = CustomUserCreationForm
    if request.method == "POST":
        form =  CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        
    context = {"form":form}
    return render(request, "register.html", context)

def portfolio(request):
    return render(request,"index.html")
