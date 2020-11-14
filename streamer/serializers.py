from rest_framework import serializers

from streamer.models import Streamer


class StreamerSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Streamer
        fields = ['id', 'name', 'surname', 'nickname']


class StreamerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Streamer
        fields = ['id', 'nickname', 'min_donation', 'account']