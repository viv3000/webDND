# Generated by Django 4.1.2 on 2022-11-01 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CharList', '0006_alter_class_dnd_description_alter_item_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='skills',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='spell_set',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
