from django.forms import ModelForm, Form
from CharList.models import Person, Person_state


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = [
            'name',
            'description',
            'race',
            'skills',
            'save_throws',
            'main_class_dnd'
        ]
        

class PersonStateForm(ModelForm):
    class Meta:
        model = Person_state
        fields = [
            #person_id
            'classes_dnd',
            'XP',
            'level',
            'hit_dice'
        ]

