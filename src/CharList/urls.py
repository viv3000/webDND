from django.urls import include, path

from .controllers import home, persons, sessions

urlpatterns = [
    path('Users', include("django.contrib.auth.urls")),

    path('', home.Home, name="Home"),


    path('Persons',                       persons.Persons, name='Persons'),
    path('Persons/View/<int:Persons_id>', persons.Person,  name="Person"),
    path('Persons/Adding',                persons.Adding,  name='Person_add'),


    path('Sessions',                         sessions.Sessions, name="Sessions"),
    path('Sessions/Adding',                  sessions.Adding,   name="Session_add"),
    path('Sessions/Table/<int:Sessions_id>', sessions.Session,  name="Session"),

    path('Sessions/Table/<int:Sessions_id>/Gamers/<int:User_id>',       sessions.Session_gamer,       name="Session_gamer"),
    path('Sessions/Table/<int:Sessions_id>/Gamers/<int:User_id>/Person',sessions.Session_gamer_person,name="Session_gamer_person"),

    path('Sessions/Table/<int:Sessions_id>/Master',                          sessions.Session_master,        name="Session_master"),
    path('Sessions/Table/<int:Sessions_id>/Master/Adding_gamer',             sessions.Session_master_adding_gamer,    name="Session_master_add"),
    path('Sessions/Table/<int:Sessions_id>/Master/Persons',                  sessions.Session_master_persons, name="Session_master_persons"),
    path('Sessions/Table/<int:Sessions_id>/Master/Persons/<int:Persons_id>', sessions.Session_master_person, name="Session_master_persons"),
]
