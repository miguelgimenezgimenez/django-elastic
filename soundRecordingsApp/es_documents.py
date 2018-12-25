from django_elasticsearch_dsl import DocType
from soundRecordingsApp.models import SoundRecording
from django.conf import settings

ES_INDEX = settings.ES_INDEX


@ES_INDEX.doc_type
class SoundRecordingDocument(DocType):
    class Meta:
        model = SoundRecording  # The model associated with this DocType

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'artist',
            'title',
            'isrc',
            'length'
        ]
