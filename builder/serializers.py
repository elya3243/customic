from rest_framework import serializers
from .models import Mockup, Dress


class DressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dress
        exclude = ('mockup', 'id')


class MockupSerializer(serializers.ModelSerializer):
    images = DressSerializer(many=True, source='dress_set', read_only=True)

    class Meta:
        model = Mockup
        exclude = ('user',)

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super(MockupSerializer, self).create(validated_data)
