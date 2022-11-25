from django.db import models
from django.contrib.auth.models import User

class Session(models.Model):
    master = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.BooleanField(default=False)
    def __str__(self):
        return 'Сессия мастера: ' + master.Username

class Item(models.Model): # item for session
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, null=True, blank=True)
    session     = models.ForeignKey(Session, on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class Save_throws(models.Model):
    description  = models.CharField(max_length=200, null=True, blank=True)
    strength     = models.CharField(max_length=200, null=True, blank=True)
    dexterity    = models.CharField(max_length=200, null=True, blank=True)
    constitution = models.CharField(max_length=200, null=True, blank=True)
    intelligence = models.CharField(max_length=200, null=True, blank=True)
    wisdom       = models.CharField(max_length=200, null=True, blank=True)
    charisma     = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.description

class Skills(models.Model):
    description     = models.CharField(max_length=200, null=True, blank=True)
    acrobatics      = models.CharField(max_length=200, null=True, blank=True)
    animal_handling = models.CharField(max_length=200, null=True, blank=True)
    arcana          = models.CharField(max_length=200, null=True, blank=True)
    athletics       = models.CharField(max_length=200, null=True, blank=True)
    deception       = models.CharField(max_length=200, null=True, blank=True)
    history         = models.CharField(max_length=200, null=True, blank=True)
    insight         = models.CharField(max_length=200, null=True, blank=True)
    intimidation    = models.CharField(max_length=200, null=True, blank=True)
    investigation   = models.CharField(max_length=200, null=True, blank=True)
    medicine        = models.CharField(max_length=200, null=True, blank=True)
    nature          = models.CharField(max_length=200, null=True, blank=True)
    perception      = models.CharField(max_length=200, null=True, blank=True)
    performance     = models.CharField(max_length=200, null=True, blank=True)
    persuasion      = models.CharField(max_length=200, null=True, blank=True)
    religion        = models.CharField(max_length=200, null=True, blank=True)
    sleight_of_hand = models.CharField(max_length=200, null=True, blank=True)
    stealth         = models.CharField(max_length=200, null=True, blank=True)
    survival        = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.description

class Spell(models.Model):
    title       = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.title

class Race(models.Model):
    title       = models.CharField(max_length=200)
    description = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.title


class Class_dnd(models.Model):
    title       = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.title

class Person(models.Model):
    main_class_dnd = models.ForeignKey(Class_dnd, on_delete=models.CASCADE, null=True)
    name           = models.CharField(max_length=200)
    description    = models.CharField(max_length=200, null=True, blank=True)
    race           = models.ForeignKey(Race, on_delete=models.CASCADE)
    user           = models.ForeignKey(User, on_delete=models.CASCADE)
    skills         = models.OneToOneField(Skills, on_delete=models.CASCADE, null=True, blank=True)
    save_throws    = models.OneToOneField(Save_throws, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name




class Person_state(models.Model):
    classes_dnd = models.ManyToManyField(Class_dnd, blank=True)
    person      = models.OneToOneField(Person, on_delete=models.CASCADE, null=True, blank=True)
    XP          = models.IntegerField(default=0)
    level       = models.IntegerField(default=1)
    hit_dice    = models.IntegerField(default=0)
    def __str__(self):
        return 'Состояние для ' + self.person.name

class Spell_set(models.Model):
    Person_state = models.ForeignKey(Person_state, on_delete=models.CASCADE)
    spell        = models.ForeignKey(Spell, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return 'Набор заклинаний для ' + self.person.name

class Group(models.Model): #dnd group
    person_state = models.ForeignKey(Person_state, on_delete=models.CASCADE)
    session      = models.ForeignKey(Session, on_delete=models.CASCADE)
    def __str__(self):
        return 'Группа сессии ' + self.session+' в которой есть ' + self.person.name


class Inventory(models.Model):
    person_state = models.OneToOneField(Person_state, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return 'Инвентарь пренадлежащий ' + self.person_state.person.name

class Item_set(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, blank=True)
    inventory = models.OneToOneField(Inventory, on_delete=models.CASCADE, null=True, blank=True);
    def __str__(self):
        return 'Предметы из: ' + self.inventory

