from django.shortcuts import render
from django.http import Http404
from rest_framework import generics
from rest_framework.response import Response

from streamer.models import Streamer, Donat
from streamer.serializers import StreamerSaveSerializer, StreamerSerializer, DonatSaveSerializer, DonatListSerializer


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

    def put(self, request, streamer_nickname):
        try:
            streamer = Streamer.objects.get(nickname=streamer_nickname)
        except Streamer.DoesNotExist:
            raise Http404
        
        streamer.min_donation = self.request.POST.get('min_donation', 10.00)
        streamer.account = self.request.POST.get('account', None)
        streamer.nickname = self.request.POST.get('nickname', streamer.nickname)
        streamer.save()
        return Response({'Message': 'Data changed succesfully!'})


class DonatCreate(generics.ListCreateAPIView):
    queryset = Donat.objects.all()
    serializer_class = DonatSaveSerializer


class DonatList(generics.ListCreateAPIView):
    queryset = Donat.objects.all()
    serializer_class = DonatListSerializer

    def get_queryset(self):
        queryset = Donat.objects.all()
        streamer_id = self.request.query_params.get('id')
        if streamer_id is not None:
            queryset = queryset.filter(streamer_id=streamer_id)
        else:
            raise Http404
        return queryset