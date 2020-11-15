from django.shortcuts import render
from django.http import Http404
from rest_framework import generics
from rest_framework.response import Response
from django.forms.models import model_to_dict

from streamer.models import Streamer, Donat
from streamer.serializers import StreamerSaveSerializer, StreamerSerializer, DonatSaveSerializer, DonatListSerializer, DonatShowSerializer


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

    # def post(self, request, streamer_nickname):
    #     try:
    #         streamer = Streamer.objects.get(nickname=streamer_nickname)
    #     except Streamer.DoesNotExist:
    #         raise Http404
        
    #     streamer.min_donation = self.request.POST.get('min_donation', 10.00)
    #     streamer.account = self.request.POST.get('account', None)
    #     streamer.nickname = self.request.POST.get('nickname', streamer.nickname)
    #     streamer.save()
    #     print(self.request.POST)
    #     print(self.request.query_params)
    #     return Response({'Message': 'Data changed succesfully!'})


class StreamerChange(generics.ListCreateAPIView):
    queryset = Streamer.objects.all()
    serializer_class = StreamerSerializer

    def get(self, request, streamer_nickname=None, **kwargs):
        try:
            streamer = Streamer.objects.get(nickname=streamer_nickname)
        except Streamer.DoesNotExist:
            raise Http404

        streamer.min_donation = self.request.query_params.get('min_donation', streamer.min_donation)
        streamer.account = self.request.query_params.get('account', streamer.account)
        streamer.nickname = self.request.query_params.get('nickname', streamer.nickname)
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


class DonatShow(generics.ListCreateAPIView):
    queryset = Donat.objects.all()
    serializer_class = DonatShowSerializer

    def get(self, request, **kwargs):
        try:
            streamer = Streamer.objects.get(token=self.request.query_params.get('token', None))
        except Streamer.DoesNotExist:
            raise Http404

        last_donat = Donat.objects.all().filter(streamer_id=streamer.id).filter(is_shown=0).order_by('create_date').first()
        last_donat.is_shown = 1
        last_donat.save()
        return Response(model_to_dict(last_donat))