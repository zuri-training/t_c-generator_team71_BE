from rest_framework import serializers

from .models import PrivacyPolicy
from users.models import User


class GetPrivacyPolicySerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(),
        queryset=User.objects.all())

    class Meta:
        model = PrivacyPolicy
        fields = '__all__'
