from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate

from CharList.models import User
from CharList.forms  import PersonForm, PersonStateForm

def Home(request):
    return render(request=request, template_name="index.html", context={})

class Sessions:
    def Sessions(request):
        return HttpResponse('Sessions')

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

class Persons:
    def Persons(request): #/Persons
        template = loader.get_template('persons/persons.html')
        context = {}
        return HttpResponse(template.render(context))

    def Person(request, Persons_id): #/Persons/View/<int>
        template = loader.get_template('persons/person.html')
        charListForm = CharListForm(request.POST)
        context = {"Perso_form": charListForm}
        return HttpResponse(template.render(context,request))
    
    def Adding(request): #/Persons/Adding
        if request.method == 'POST':
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is None:
                return render(request, 'registration/login.html', {})
            else:
                return render(request, 'persons/adding.html', {})
        else:
            template = loader.get_template('persons/adding.html')
            return HttpResponse(template.render({}, request))
                    
