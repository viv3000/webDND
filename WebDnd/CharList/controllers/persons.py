from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate

from CharList.models import User
from CharList.forms  import PersonForm, PersonStateForm

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
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        if request.method == 'POST':
            personForm = PersonForm(request.POST or None)
            personStateForm = PersonStateForm(request.POST or None)
            if personStateForm.is_valid and personForm.is_valid:
                personForm.save(commit=False)
                personForm.user = request.user
                personForm.save()
    
                personStateForm.save(commit=False)
                personStateForm.person = personForm.id
                personStateForm.save()
    
                return redirect('Persons')
            else:
                return redirect('Persons/Adding')
        else: 
            template = 'persons/adding.html'
            personForm = PersonForm()
            personStateForm = PersonStateForm();
    
            context = {
                    'Person_form': personForm,
                    'Person_state_form': personStateForm
            }
            return render(request, template, context)
    else:
        return 'auth'
"""
    template = loader.get_template("persons/adding.html")
    charListForm = PersonForm(request.POST)
    context = {"Person_form": charListForm}
    return HttpResponse(template.render(context,request))
"""
