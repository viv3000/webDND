# Generated by Django 4.1.3 on 2022-11-16 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CharList', '0013_save_throws_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classes_dnd',
            name='person',
        ),
        migrations.AddField(
            model_name='person',
            name='classes_dnd',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CharList.classes_dnd'),
        ),
    ]
