# Generated by Django 5.1.4 on 2025-01-09 22:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Player', '0002_remove_player_email_remove_player_first_name_and_more'),
        ('invitation_app', '0004_geocoordinates_player_proposeddate_sport_and_more'),
        ('sport_app', '0002_remove_sport_titre_sport_sp_titre_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='player_b',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_invitations', to='Player.player'),
        ),
        migrations.AlterField(
            model_name='invitation',
            name='player_a',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_invitations', to='Player.player'),
        ),
        migrations.AlterField(
            model_name='invitation',
            name='sport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sport_app.sport'),
        ),
        migrations.DeleteModel(
            name='Player',
        ),
        migrations.DeleteModel(
            name='Sport',
        ),
    ]
