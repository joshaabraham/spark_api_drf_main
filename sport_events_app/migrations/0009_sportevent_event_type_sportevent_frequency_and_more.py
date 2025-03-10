# Generated by Django 5.1.4 on 2025-03-10 22:07

import sport_events_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport_events_app', '0008_match_album_sportevent_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='sportevent',
            name='event_type',
            field=models.CharField(choices=[(sport_events_app.models.EventType['INDIVIDUAL'], 'Individual'), (sport_events_app.models.EventType['TEAM'], 'Team'), (sport_events_app.models.EventType['MIXED'], 'Mixed')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sportevent',
            name='frequency',
            field=models.CharField(choices=[(sport_events_app.models.Frequency['ANNUAL'], 'Annual'), (sport_events_app.models.Frequency['BIENNIAL'], 'Biennial'), (sport_events_app.models.Frequency['QUADRENNIAL'], 'Quadrennial'), (sport_events_app.models.Frequency['ONE_TIME'], 'One-time')], default=4, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sportevent',
            name='geographic_scope',
            field=models.CharField(choices=[(sport_events_app.models.GeographicScope['LOCAL'], 'Local'), (sport_events_app.models.GeographicScope['NATIONAL'], 'National'), (sport_events_app.models.GeographicScope['CONTINENTAL'], 'Continental'), (sport_events_app.models.GeographicScope['INTERNATIONAL'], 'International')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sportevent',
            name='objective',
            field=models.CharField(choices=[(sport_events_app.models.Objective['PROFESSIONAL'], 'Professional'), (sport_events_app.models.Objective['AMATEUR'], 'Amateur'), (sport_events_app.models.Objective['CHARITY'], 'Charity')], default=2, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sportevent',
            name='sport_type',
            field=models.CharField(choices=[(sport_events_app.models.SportType['TEAM_SPORTS'], 'Team sports'), (sport_events_app.models.SportType['INDIVIDUAL_SPORTS'], 'Individual sports'), (sport_events_app.models.SportType['MOTOR_SPORTS'], 'Motor sports'), (sport_events_app.models.SportType['EXTREME_SPORTS'], 'Extreme sports')], default=2, max_length=50),
            preserve_default=False,
        ),
    ]
