# Generated by Django 5.1.7 on 2025-03-26 15:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abonnement_app', '0003_alter_payment_subscription_alter_payment_user_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='stripe_subscription_id',
        ),
        migrations.AlterField(
            model_name='payment',
            name='stripe_charge_id',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='payment',
            name='subscription',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='abonnement_app.subscription'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='plan',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='stripe_customer_id',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Payout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_payout_id', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_transfer_id', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('commission', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('destination_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transfers_received', to=settings.AUTH_USER_MODEL)),
                ('source_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transfers_sent', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='PaymentCard',
        ),
    ]
