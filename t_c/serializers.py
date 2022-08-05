from rest_framework import serializers

from .models import Terms
from users.models import User


class GetTCSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(),
        queryset=User.objects.all())

    class Meta:
        model = Terms
        fields = '__all__'



