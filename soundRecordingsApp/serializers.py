from rest_framework import serializers
from soundRecordingsApp.models import SoundRecording


class SoundRecordingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoundRecording
        fields = ('artist', 'title', 'isrc', 'length')
