# Generated by Django 4.1.2 on 2022-11-01 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CharList', '0004_remove_person_state_save_throws_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='race',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
