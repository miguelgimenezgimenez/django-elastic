from rest_framework import serializers
from soundRecordingsApp.models import SoundRecording, SoundRecordingInput


class SoundRecordingModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = SoundRecording
		fields =  '__all__'

class SoundRecordingInputModelSerializer(serializers.ModelSerializer):
	matches = SoundRecordingModelSerializer(many=True, read_only=True)

	class Meta:
		model = SoundRecordingInput
		fields =  '__all__'

