# Generated by Django 4.0.6 on 2022-10-29 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CharList', '0002_session_activity'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='title',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
