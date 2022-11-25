# Generated by Django 4.1.3 on 2022-11-13 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CharList', '0009_remove_person_person_state_person_state_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person_state',
            name='person',
        ),
        migrations.AddField(
            model_name='person',
            name='person_state',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CharList.person_state'),
        ),
    ]
