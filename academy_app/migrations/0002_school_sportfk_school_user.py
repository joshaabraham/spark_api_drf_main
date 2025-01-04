# Generated by Django 4.1.7 on 2024-09-08 13:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sport_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('academy_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='sportFK',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='shool', to='sport_app.sport'),
        ),
        migrations.AddField(
            model_name='school',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='school', to=settings.AUTH_USER_MODEL),
        ),
    ]