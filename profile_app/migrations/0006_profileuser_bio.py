# Generated by Django 5.1.7 on 2025-03-27 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0005_rename_profile_image_profileuser_avatar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileuser',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]
