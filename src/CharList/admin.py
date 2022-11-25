from django.contrib import admin

from .models import Spell, Class_dnd, Person, Race, Person_state, Skills, Save_throws, Inventory, Item_set, Item, Session, Group, Spell_set

admin.site.register(Spell)
admin.site.register(Class_dnd)
admin.site.register(Person)
admin.site.register(Race)
admin.site.register(Person_state)
admin.site.register(Skills)
admin.site.register(Save_throws)
admin.site.register(Inventory)
admin.site.register(Item_set)
admin.site.register(Item)
admin.site.register(Session)
admin.site.register(Group)
admin.site.register(Spell_set)
