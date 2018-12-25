from django_elasticsearch_dsl_drf.pagination import PageNumberPagination
from django_elasticsearch_dsl_drf.views import BaseDocumentViewSet
from soundRecordingsApp.es_documents import SoundRecordingDocument
from soundRecordingsApp.es_serializers import SoundRecordingDocumentSimpleSerializer


class ESSoundRecordingViewSet(BaseDocumentViewSet):
    document = SoundRecordingDocument
    serializer_class = SoundRecordingDocumentSimpleSerializer
    pagination_class = PageNumberPagination
    paginate_by = 30
