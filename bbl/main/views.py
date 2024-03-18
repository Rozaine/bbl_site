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
    userform = TicketForm()
    form = TicketForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('/succsess')
        return render(request, "about.html", {"form": userform})
    else:
        return render(request, "about.html", {"form": userform})


def service(request):
    userform = TicketForm()
    form = TicketForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('/succsess')
        return render(request, "services.html", {"form": userform})
    else:
        return render(request, "services.html", {"form": userform})


def phy_sec(request):
    userform = TicketForm()
    form = TicketForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('/succsess')
        return render(request, "physical_security.html", {"form": userform})
    else:
        return render(request, "physical_security.html", {"form": userform})


def video_sec(request):
    userform = TicketForm()
    form = TicketForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('/succsess')
        return render(request, "video_ser.html", {"form": userform})
    else:
        return render(request, "video_ser.html", {"form": userform})



def radio_sec(request):
    userform = TicketForm()
    form = TicketForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('/succsess')
        return render(request, "radio_ser.html", {"form": userform})
    else:
        return render(request, "radio_ser.html", {"form": userform})



def cargo_sec(request):
    userform = TicketForm()
    form = TicketForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('/succsess')
        return render(request, "cargo.html", {"form": userform})
    else:
        return render(request, "cargo.html", {"form": userform})


def portfolio(request):
    userform = TicketForm()
    form = TicketForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('/succsess')
        return render(request, "projects.html", {"form": userform})
    else:
        return render(request, "projects.html", {"form": userform})


def contacts(request):
    userform = TicketForm()
    form = TicketForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('/succsess')
        return render(request, "contacts.html", {"form": userform})
    else:
        return render(request, "contacts.html", {"form": userform})


def vacancies(request):
    userform = TicketForm()
    form = TicketForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('/succsess')
        return render(request, "vacancies.html", {"form": userform})
    else:
        return render(request, "vacancies.html", {"form": userform})


def succsess(request):
    return render(request, "succsess.html")

