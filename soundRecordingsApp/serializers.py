from rest_framework import serializers
from soundRecordingsApp.models import SoundRecording,SoundRecordingInput


class SoundRecordingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoundRecording
        fields = ('artist', 'title', 'isrc', 'length')

class SoundRecordingInputModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoundRecordingInput
        fields = ('artist', 'title', 'isrc', 'length','matches')
