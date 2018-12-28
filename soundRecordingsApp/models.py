from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.contrib.auth.models import User




class BaseModelInterface(models.Model):
	artist = models.CharField(max_length=300, blank=True)
	 
	title = models.CharField(max_length=300, blank=True)
	
	isrc = models.CharField(max_length=18, blank=True)

	length = models.CharField(max_length=12, blank=True)

	class Meta:
		abstract = True


@python_2_unicode_compatible
class SoundRecording(BaseModelInterface):
	
	def __str__(self):
		return "Title: {0} Artist: {1}".format(self.title, self.artist)


@python_2_unicode_compatible
class SoundRecordingInput(BaseModelInterface):

	matches = models.ManyToManyField(SoundRecording, through='SimilarityScores',related_name='matchesByScore')

	selectedCandidate = models.ForeignKey (
			SoundRecording,
			on_delete=models.SET_NULL,
			null=True
		)
	def __str__(self):
		return "Title: {0} Aritist: {1}".format(self.title, self.artist)
		
@python_2_unicode_compatible
class SimilarityScores(models.Model):

	soundRecording = models.ForeignKey(SoundRecording, on_delete=models.CASCADE, related_name='soundRecordingMatches')
	
	soundRecordingInput = models.ForeignKey(SoundRecordingInput, on_delete=models.CASCADE, related_name='soundInputMatches')

	score = models.IntegerField()

	