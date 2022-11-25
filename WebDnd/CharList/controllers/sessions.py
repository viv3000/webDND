from django.http import HttpResponse
from django.shortcuts import render

def Sessions(request):
    template_path = "sessions/sessions.html"
    sessions = [1,2,3,4,5]
    context = {
        "sessions": sessions,
    }
    return render(request=request, template_name=template_path, context=context)

def Adding(request):
    return HttpResponse("Adding");

def Session(request, Sessions_id):
    return HttpResponse("Session")


def Session_gamer(request, Sessions_id, User_id):
    return HttpResponse("Gamer")

def Session_gamer_person(request, Sessions_id, User_id):
    return HttpResponse("Gamer person")


def Session_master(request, Sessions_id):
    return HttpResponse("Master")

def Session_master_adding_gamer(request, Sessions_id):
    return HttpResponse("Master")

def Session_master_persons(request, Sessions_id):
    return HttpResponse("Master")

def Session_master_person(request, Sessions_id, Persons_id):
    return HttpResponse("Master")




