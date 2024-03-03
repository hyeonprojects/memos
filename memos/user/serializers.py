from rest_framework import serializers

from memos.user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at', 'deleted_at']
        extra_kwargs = {
            'password': {'write_only': True}
        }

