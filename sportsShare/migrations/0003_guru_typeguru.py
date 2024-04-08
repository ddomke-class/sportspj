# Generated by Django 4.2 on 2024-04-08 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportsShare', '0002_remove_guru_major_guru_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='guru',
            name='typeguru',
            field=models.CharField(choices=[('Bar Owner', 'Matchup Stats'), ('Analyst', 'Team Comparison'), ('Gambler', 'Single Player Stats'), ('Newbie', 'Exploring a New World')], default='Newbie', max_length=200),
        ),
    ]
