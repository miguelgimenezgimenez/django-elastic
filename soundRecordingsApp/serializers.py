from rest_framework import serializers
from soundRecordingsApp.models import SoundRecording, SoundRecordingInput, SimilarityScores


class SoundRecordingModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = SoundRecording
		fields =  '__all__'

class SoundRecordingInputModelSerializer(serializers.ModelSerializer):
	matches = SoundRecordingMatchSerializer(many=True, read_only=True)

	class Meta:
		model = SoundRecordingInput
		fields =  '__all__'




class SoundRecordingMatchSerializer(serializers.ModelSerializer):
	score = serializers.IntegerField(read_only=True)

	class Meta:
		model = SoundRecording
		fields =  '__all__'


class SoundRecordingInputMatchesSerializer(serializers.ModelSerializer):
	matches = serializers.SerializerMethodField()

	class Meta:
		model = SoundRecordingInput
		fields =  '__all__'
	# I am not sure this is the most efficient way.
	def get_matches(self, obj):

			matches = []

			similarityScores = SimilarityScores.objects.filter(soundRecordingInput_id=obj.id)
			
			for match in similarityScores :
				
				soundRecording = SoundRecording.objects.get(id=match.soundRecording.id)
				
				soundRecording.score = match.score
				
				serializer = SoundRecordingMatchSerializer(soundRecording)
				matches.append(serializer.data)

			return matches

			