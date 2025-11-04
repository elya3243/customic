from rest_framework import serializers
from .models import Mockup


class MockupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mockup
        fields = '__all__'

    def create(self, validated_data):
        if self.context['request'].user.is_authenticated:
            validated_data['user'] = self.context['request'].user
        return super(MockupSerializer, self).create(validated_data)