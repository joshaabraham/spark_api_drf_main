# Generated by Django 5.1.4 on 2025-03-10 22:08

import sport_events_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport_events_app', '0009_sportevent_event_type_sportevent_frequency_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sportevent',
            name='event_type',
            field=models.CharField(choices=[(sport_events_app.models.EventType['INDIVIDUAL'], 'Individual'), (sport_events_app.models.EventType['TEAM'], 'Team'), (sport_events_app.models.EventType['MIXED'], 'Mixed')], default='Individual', max_length=50),
        ),
    ]
