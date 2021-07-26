from django.shortcuts import render


def home(request):
    return render(request, "core/home.html")


def assignment(request):
    return render(request, "core/assignment.html")


def service(request):
    return render(request, "core/service.html")
