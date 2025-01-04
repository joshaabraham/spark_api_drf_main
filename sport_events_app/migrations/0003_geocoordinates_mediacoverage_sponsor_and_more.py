# Generated by Django 5.1.4 on 2025-01-03 23:05

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Player', '0001_initial'),
        ('equipe_app', '0002_remove_team_founded_team_budget_and_more'),
        ('sport_app', '0002_remove_sport_titre_sport_sp_titre_en_and_more'),
        ('sport_events_app', '0002_sportevent_sportfk'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeoCoordinates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='MediaCoverage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_outlet', models.CharField(max_length=255)),
                ('coverage_type', models.CharField(max_length=100)),
                ('coverage_details', models.TextField(blank=True, null=True)),
                ('coverage_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('industry', models.CharField(max_length=100)),
                ('contribution_amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('logo_url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='sportevent',
            old_name='event_date',
            new_name='start_date',
        ),
        migrations.RemoveField(
            model_name='sportevent',
            name='sportFK',
        ),
        migrations.RemoveField(
            model_name='sportevent',
            name='user',
        ),
        migrations.AddField(
            model_name='sportevent',
            name='end_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sportevent',
            name='estimated_audience',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sportevent',
            name='is_recurring',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sportevent',
            name='notable_players',
            field=models.ManyToManyField(related_name='notable_events', to='Player.player'),
        ),
        migrations.AddField(
            model_name='sportevent',
            name='organizer',
            field=models.CharField(default='me', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sportevent',
            name='participating_teams',
            field=models.ManyToManyField(related_name='events', to='equipe_app.team'),
        ),
        migrations.AddField(
            model_name='sportevent',
            name='recurrence_interval_years',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sportevent',
            name='sports',
            field=models.ManyToManyField(related_name='events', to='sport_app.sport'),
        ),
        migrations.AlterField(
            model_name='sportevent',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AddField(
            model_name='sportevent',
            name='coordinates',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sport_events', to='sport_events_app.geocoordinates'),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField(blank=True, null=True)),
                ('coordinates', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='location', to='sport_events_app.geocoordinates')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_date', models.DateTimeField()),
                ('result', models.CharField(blank=True, max_length=50, null=True)),
                ('key_players', models.ManyToManyField(related_name='key_matches', to='Player.player')),
                ('team_a', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches_as_team_a', to='equipe_app.team')),
                ('team_b', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches_as_team_b', to='equipe_app.team')),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches', to='sport_events_app.location')),
            ],
        ),
        migrations.AddField(
            model_name='sportevent',
            name='matches',
            field=models.ManyToManyField(related_name='sport_events', to='sport_events_app.match'),
        ),
        migrations.AddField(
            model_name='sportevent',
            name='media_coverage_details',
            field=models.ManyToManyField(related_name='covered_events', to='sport_events_app.mediacoverage'),
        ),
        migrations.AddField(
            model_name='sportevent',
            name='sponsors',
            field=models.ManyToManyField(related_name='sponsored_events', to='sport_events_app.sponsor'),
        ),
    ]
