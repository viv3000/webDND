# Generated by Django 4.1.3 on 2022-11-16 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CharList', '0014_remove_classes_dnd_person_person_classes_dnd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='classes_dnd',
        ),
        migrations.AddField(
            model_name='classes_dnd',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CharList.person'),
        ),
        migrations.AlterField(
            model_name='class_dnd',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='classes_dnd',
            name='class_dnd',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CharList.class_dnd'),
        ),
    ]
