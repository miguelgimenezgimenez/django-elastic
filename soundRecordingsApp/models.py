from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

from django.contrib.auth.models import User




@python_2_unicode_compatible
class SoundRecording(models.Model):

	artist = models.CharField(max_length=300, blank=True)
	 
	title = models.CharField(max_length=300, blank=True)
	
	isrc = models.CharField(max_length=12, blank=True)

	length = models.CharField(max_length=12, blank=True)
	
   
class SoundRecordingInput(SoundRecording):

	matches = models.ManyToManyField(SoundRecording, through='SimilarityScores',related_name='matchesByScore')

	def getSimilarityScores(self):
		soundRecording = SoundRecording.objects.all()
		# for recording in soundRecording:					
			

class SimilarityScores(models.Model):

	soundRecording = models.ForeignKey(SoundRecording, on_delete=models.CASCADE, related_name='soundRecordingMatches')
	
	soundRecordingInput = models.ForeignKey(SoundRecordingInput, on_delete=models.CASCADE, related_name='soundInputMatches')
	score = models.IntegerField()
	