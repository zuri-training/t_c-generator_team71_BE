from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

from users.models import User


# # Create your models here.

class PrivacyPolicy(models.Model):
    """
    This is the model for the terms and conditions template
    """
    user_id = models.ForeignKey(User, related_name='privacy_policies', on_delete=models.CASCADE)
    business_name = models.CharField(max_length=200, null=False, blank=False)
    business_url = models.URLField(unique=True)
    document_name = models.CharField(null=False, blank=False, max_length=224)
    contact_email = models.EmailField(null=False, blank=False)
    contact_phone = PhoneNumberField(null=False, blank=False)
    consent = models.BooleanField(null=True, blank=True)
    info_we_collect = models.BooleanField(null=True, blank=True)
    how_we_use_info = models.BooleanField(null=True, blank=True)
    cookies = models.BooleanField(null=True, blank=True)
    advertising_partners = models.BooleanField(null=True, blank=True)
    third_party = models.BooleanField(null=True, blank=True)
    children_information = models.BooleanField(null=True, blank=True)
    permanent = models.BooleanField(null=True, blank=True)
    create_date = models.DateTimeField(null=True)
    last_edit = models.DateTimeField(null=True)

    class Meta:
        ordering = ['last_edit']

