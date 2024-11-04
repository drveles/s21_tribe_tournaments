# Generated by Django 5.1 on 2024-08-23 18:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s21_tribe_tournaments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='peers',
            old_name='campus_id',
            new_name='campus',
        ),
        migrations.RenameField(
            model_name='tribes',
            old_name='campus_id',
            new_name='campus',
        ),
        migrations.RemoveField(
            model_name='peers',
            name='curr_tribe_id',
        ),
        migrations.RemoveField(
            model_name='peers',
            name='prev_tribe_id',
        ),
        migrations.AddField(
            model_name='peers',
            name='curr_tribe',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='curr_tribe', to='s21_tribe_tournaments.tribes'),
        ),
        migrations.AddField(
            model_name='peers',
            name='prev_tribe',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prev_tribe', to='s21_tribe_tournaments.tribes'),
        ),
        migrations.AlterField(
            model_name='campuses',
            name='slug',
            field=models.CharField(max_length=52, unique=True),
        ),
        migrations.AlterField(
            model_name='tribes',
            name='slug',
            field=models.CharField(max_length=21, unique=True),
        ),
    ]