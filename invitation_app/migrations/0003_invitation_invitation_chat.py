# Generated by Django 4.1.7 on 2024-10-16 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0002_rename_datecreation_chat_created_at_and_more'),
        ('invitation_app', '0002_invitation_sport'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitation',
            name='invitation_chat',
            field=models.ForeignKey(blank=True, max_length=255, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invitations', to='chat_app.chat'),
        ),
    ]