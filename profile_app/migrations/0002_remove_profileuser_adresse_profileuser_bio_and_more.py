# Generated by Django 4.1.7 on 2024-09-15 11:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profile_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profileuser',
            name='adresse',
        ),
        migrations.AddField(
            model_name='profileuser',
            name='bio',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profileuser',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profileuser',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='cover_pics/'),
        ),
        migrations.AddField(
            model_name='profileuser',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='profileuser',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='followers_set', to='profile_app.profileuser'),
        ),
        migrations.AddField(
            model_name='profileuser',
            name='followers_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profileuser',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='following_set', to='profile_app.profileuser'),
        ),
        migrations.AddField(
            model_name='profileuser',
            name='following_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profileuser',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='friend_set', to='profile_app.profileuser'),
        ),
        migrations.AddField(
            model_name='profileuser',
            name='friends_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profileuser',
            name='is_private',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profileuser',
            name='location',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='profileuser',
            name='posts_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profileuser',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/'),
        ),
        migrations.AddField(
            model_name='profileuser',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profileuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
