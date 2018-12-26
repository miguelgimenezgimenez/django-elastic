from django.contrib import admin

# Register your models here.
from .models import SoundRecording, SoundRecordingInput, SimilarityScores

class SoundRecordingAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist','isrc', 'length')

class SimilarityScoresAdmin(admin.ModelAdmin):
    list_display = ('soundRecording', 'soundRecordingInput','score')

admin.site.register(SoundRecording,SoundRecordingAdmin)
admin.site.register(SoundRecordingInput,SoundRecordingAdmin)
admin.site.register(SimilarityScores, SimilarityScoresAdmin)
