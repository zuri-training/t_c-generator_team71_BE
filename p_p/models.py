from django.db import models

# Create your models here.

from users.models import User


# # Create your models here.

class PrivacyPolicy(models.Model):
    """
    This is the model for the terms and conditions template
    """
    user_id = models.ForeignKey(User, related_name='privacy_policies', on_delete=models.CASCADE)
    business_name = models.CharField(max_length=200, null=True, blank=True)
    business_url = models.URLField(unique=True)
    country = models.CharField(max_length=30, null=True, blank=True)
    state = models.CharField(max_length=30, null=True, blank=True)
    additional_info = models.TextField(null=True, blank=True)
    marketing_services = models.CharField(max_length=300, null=True, blank=True)
    tracking_services = models.CharField(max_length=300, null=True, blank=True)
    captcha_service = models.CharField(max_length=300, null=True, blank=True)
    contact_info = models.EmailField(null=True, blank=True)
    permanent = models.BooleanField(null=True, blank=True)
    create_date = models.DateTimeField(null=True)
    last_edit = models.DateTimeField(null=True)

    class Meta:
        ordering = ['last_edit']

