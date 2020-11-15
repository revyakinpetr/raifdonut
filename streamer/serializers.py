from rest_framework import serializers

from streamer.models import Streamer, Donat


class StreamerSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Streamer
        fields = ['id', 'name', 'surname', 'nickname']


class StreamerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Streamer
        fields = ['id', 'nickname', 'min_donation', 'account', 'token']


class DonatSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donat
        fields = ['id', 'streamer_id', 'name', 'text', 'amount']


class DonatListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donat
        fields = ['id', 'streamer_id', 'name', 'text', 'amount', 'create_date']


class DonatShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donat
        fields = ['id', 'name', 'text', 'amount', 'create_date', 'is_shown']