# Generated by Django 4.0.6 on 2022-10-29 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CharList', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='activity',
            field=models.BooleanField(default=False),
        ),
    ]
