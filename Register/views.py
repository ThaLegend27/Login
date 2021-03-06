from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
        return redirect("/home")
    else:
        form = RegisterForm()
    return render(response, "Register/Register.html", {"form":form})