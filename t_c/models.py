from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from users.models import User

# # Create your models here.

class Terms(models.Model):
    """
    This is the model for the terms and conditions template
    """
    user_id = models.ForeignKey(User, related_name='terms', on_delete=models.CASCADE)
    business_name = models.CharField(max_length=200, null=False, blank=False)
    business_url = models.URLField(unique=True)
    document_name = models.CharField(null=False, blank=False, max_length=224)
    contact_email = models.EmailField(null=False, blank=False)
    contact_phone = PhoneNumberField(null=False, blank=False)
    cookies = models.BooleanField(null=True, blank=True)
    licenses = models.BooleanField(null=True, blank=True)
    content_liability = models.BooleanField(null=True, blank=True)
    iframes = models.BooleanField(null=True, blank=True)
    disclaimer = models.BooleanField(null=True, blank=True)
    additional_text = models.TextField(null=True, blank=True)
    permanent = models.BooleanField(null=False, blank=False)
    create_date = models.DateTimeField(null=True, blank=True)
    last_edit = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['last_edit']

# Create your models here.

