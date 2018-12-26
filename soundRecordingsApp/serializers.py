from rest_framework import serializers
from soundRecordingsApp.models import SoundRecording,SoundRecordingInput


class SoundRecordingModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = SoundRecording
		fields = ('id','artist', 'title', 'isrc', 'length')

class SoundRecordingInputModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = SoundRecordingInput
		fields = ('id','artist', 'title', 'isrc', 'length','matches')

	# def create(self, validated_data):
	# 	obj = SoundRecordingInput.objects.create(**validated_data)
	# 	print(validated_data,'CRREEAAAAATEEEE')
	# 	return obj
