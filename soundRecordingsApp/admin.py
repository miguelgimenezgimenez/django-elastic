from django.contrib import admin

# Register your models here.
from .models import SoundRecording, SoundRecordingInput, SimilarityScores

admin.site.register(SoundRecording)
admin.site.register(SoundRecordingInput)
admin.site.register(SimilarityScores)
