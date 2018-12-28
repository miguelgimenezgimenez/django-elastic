from rest_framework import routers

from soundRecordingsApp import views
from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('soundrecording', views.SoundRecordingList.as_view()),
    path('soundrecordingInput', views.SoundRecordingInputList.as_view()),
    # path('soundrecording/<int:pk>/', views.SoundRecordingDetail.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)

