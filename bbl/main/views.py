from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import TicketForm


def index(request):
    userform = TicketForm()
    form = TicketForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('/succsess')
        return render(request, "index.html", {"form": userform})
    else:
        return render(request, "index.html", {"form": userform})




def about(request):
    return render(request, "about.html")


def service(request):
    return render(request, "services.html")


def phy_sec(request):
    return render(request, "physical_security.html")


def video_sec(request):
    return render(request, "video_ser.html")


def radio_sec(request):
    return render(request, "radio_ser.html")


def cargo_sec(request):
    return render(request, "cargo.html")


def portfolio(request):
    return render(request, "projects.html")


def contacts(request):
    return render(request, "contacts.html")


def vacancies(request):
    return render(request, "vacancies.html")

def succsess(request):
    return render(request, "succsess.html")

