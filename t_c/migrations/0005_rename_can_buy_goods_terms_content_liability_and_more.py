# Generated by Django 4.0.6 on 2022-08-08 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('t_c', '0004_alter_terms_age_limit_alter_terms_create_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='terms',
            old_name='can_buy_goods',
            new_name='content_liability',
        ),
        migrations.RenameField(
            model_name='terms',
            old_name='can_create_acct',
            new_name='cookies',
        ),
        migrations.RenameField(
            model_name='terms',
            old_name='use_feedback',
            new_name='disclaimer',
        ),
        migrations.RemoveField(
            model_name='terms',
            name='age_limit',
        ),
        migrations.RemoveField(
            model_name='terms',
            name='business_address',
        ),
        migrations.RemoveField(
            model_name='terms',
            name='contact_info',
        ),
        migrations.RemoveField(
            model_name='terms',
            name='country',
        ),
        migrations.RemoveField(
            model_name='terms',
            name='state',
        ),
        migrations.AddField(
            model_name='terms',
            name='iframes',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='terms',
            name='licenses',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
