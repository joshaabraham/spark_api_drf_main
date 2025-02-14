# Generated by Django 5.1.4 on 2025-02-08 15:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images_app', '0003_alter_album_cover_image_alter_photo_image'),
        ('sport_events_app', '0007_alter_sportevent_adresse'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='album',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='match_album', to='images_app.album'),
        ),
        migrations.AddField(
            model_name='sportevent',
            name='album',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_album', to='images_app.album'),
        ),
    ]
