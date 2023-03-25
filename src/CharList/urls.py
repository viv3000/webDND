from django.urls import include, path

from .views import Home, Persons, Sessions

urlpatterns = [
    path('Users/', include("django.contrib.auth.urls")),

    path('', Home, name="Home"),


    path('Persons',                       Persons.Persons, name='Persons'),
    path('Persons/View/<int:Persons_id>', Persons.Person,  name="Person"),
    path('Persons/Adding',                Persons.Adding,  name='Person_add'),


    path('Sessions',                         Sessions.Sessions, name="Sessions"),
    path('Sessions/Adding',                  Sessions.Adding,   name="Session_add"),

    path('Sessions/Table/<int:Sessions_id>', Sessions.Session,  name="Session"),

    path('Sessions/Table/<int:Sessions_id>/Gamers/<int:User_id>',       Sessions.Session_gamer,       name="Session_gamer"),
    path('Sessions/Table/<int:Sessions_id>/Gamers/<int:User_id>/Person',Sessions.Session_gamer_person,name="Session_gamer_person"),

    path('Sessions/Table/<int:Sessions_id>/Master',                          Sessions.Session_master,        name="Session_master"),
    path('Sessions/Table/<int:Sessions_id>/Master/Adding_gamer',             Sessions.Session_master_adding_gamer,    name="Session_master_add"),
    path('Sessions/Table/<int:Sessions_id>/Master/Persons',                  Sessions.Session_master_persons, name="Session_master_persons"),
    path('Sessions/Table/<int:Sessions_id>/Master/Persons/<int:Persons_id>', Sessions.Session_master_person, name="Session_master_persons"),
]
