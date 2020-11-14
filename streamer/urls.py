from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from streamer import views

urlpatterns = [
    path('registration', views.StreamerCreate.as_view()),
    path('donate/<str:streamer_nickname>', views.StreamerPage.as_view()),
    path('donation', views.DonatCreate.as_view()),
    path('alldonation', views.DonatList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
