from rest_framework import serializers
from .models import TestUser

class TestUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestUser
        fields = ['username', 'email', 'phone_number', 'password', 'token', 'created_at']

    def validate(self, data):
        # At least one of username/email/phone must be provided
        if not (data.get('username') or data.get('email') or data.get('phone_number')):
            raise serializers.ValidationError(
                "At least one of username, email, or phone number must be provided."
            )
        # Token is optional, so i did not validate it
        return data
