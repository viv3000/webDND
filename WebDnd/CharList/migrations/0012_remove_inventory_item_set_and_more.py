# Generated by Django 4.1.3 on 2022-11-16 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CharList', '0011_remove_person_person_state_person_state_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='item_set',
        ),
        migrations.RemoveField(
            model_name='person_state',
            name='inventory',
        ),
        migrations.AddField(
            model_name='inventory',
            name='person_state',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CharList.person_state'),
        ),
        migrations.AddField(
            model_name='item_set',
            name='inventory',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CharList.inventory'),
        ),
        migrations.AlterField(
            model_name='person',
            name='save_throws',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CharList.save_throws'),
        ),
        migrations.AlterField(
            model_name='person',
            name='skills',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CharList.skills'),
        ),
    ]
