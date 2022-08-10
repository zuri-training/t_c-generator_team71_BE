# Generated by Django 4.0.6 on 2022-08-08 13:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('p_p', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='privacypolicy',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='privacy_policies', to=settings.AUTH_USER_MODEL),
        ),
    ]
