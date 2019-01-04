from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.contrib.auth.models import User
from subprocess import call



class BaseModelInterface(models.Model):
	artist = models.CharField(max_length=300, blank=True)
	 
	title = models.CharField(max_length=300, blank=True)
	
	isrc = models.CharField(max_length=18, blank=True)

	length = models.CharField(max_length=12, blank=True)

	class Meta:
		abstract = True


class SoundRecordingInputModelManager(models.Manager):
	# OVERRIDE the bulk_create method to update elastic search indexes.
	def bulk_create(self, *args, **kwargs):		
		super().bulk_create(*args,*kwargs)
		# This is a very ugly hack, since the search index is only updated when calling save,but not on bulk_create, there has to be a better way to do this, havent had the time to figure out.
		call(['python', 'manage.py', 'search_index', '--populate' ])



@python_2_unicode_compatible
class SoundRecording(BaseModelInterface):
	objects = SoundRecordingInputModelManager()
	def __str__(self):
		return "Title: {0} Artist: {1}".format(self.title, self.artist)


@python_2_unicode_compatible
class SoundRecordingInput(BaseModelInterface):

	matches = models.ManyToManyField(SoundRecording, through='SimilarityScores',related_name='matchesByScore')

	selectedCandidate = models.ForeignKey (
			SoundRecording,
			on_delete=models.SET_NULL,
			null=True,
			blank=True
		)
	def __str__(self):
		return "Title: {0} Aritist: {1}".format(self.title, self.artist)
		
@python_2_unicode_compatible
class SimilarityScores(models.Model):

	soundRecording = models.ForeignKey(SoundRecording, on_delete=models.CASCADE, related_name='soundRecordingMatches')
	
	soundRecordingInput = models.ForeignKey(SoundRecordingInput, on_delete=models.CASCADE, related_name='soundInputMatches')

	score = models.IntegerField()

	