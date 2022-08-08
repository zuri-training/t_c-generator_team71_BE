# Generated by Django 4.0.6 on 2022-08-08 10:18

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('p_p', '0005_remove_privacypolicy_additional_info_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='privacypolicy',
            name='contact_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='privacypolicy',
            name='contact_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
    ]