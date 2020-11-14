from django.shortcuts import render
from django.http import Http404
from rest_framework import generics
from rest_framework.response import Response

from streamer.models import Streamer
from streamer.serializers import StreamerSaveSerializer, StreamerSerializer


class StreamerCreate(generics.ListCreateAPIView):
    queryset = Streamer.objects.all()
    serializer_class = StreamerSaveSerializer


class StreamerPage(generics.RetrieveUpdateDestroyAPIView):
    queryset = Streamer.objects.all()
    serializer_class = StreamerSerializer

    def get(self, request, streamer_nickname=None, **kwargs):
        try:
            streamer = Streamer.objects.get(nickname=streamer_nickname)
        except Streamer.DoesNotExist:
            raise Http404
        serializer = StreamerSerializer(streamer)
        return Response(serializer.data)