from soundRecordingsApp.models import SoundRecording, SoundRecordingInput

from soundRecordingsApp.serializers import SoundRecordingInputModelSerializer




from .es_documents import SoundRecordingDocument
from elasticsearch_dsl import Q


def getMatches(soundRecordingInputs):
	serializer = SoundRecordingInputModelSerializer(soundRecordingInputs, many=True)
	for inputRecording in serializer.data:
		artist =inputRecording.get('title') 
		title =inputRecording.get('title')
		isrc =inputRecording.get('isrc')
		isrc =inputRecording.get('isrc')
		length =inputRecording.get('length')

		q = Q('bool',should=[
			Q("multi_match", query=artist, fields=['artist'], fuzziness="AUTO", boost=0.5),
			Q("multi_match", query=title, fields=['title'], fuzziness="AUTO", boost=0.5),
			Q("multi_match", query=isrc, fields=['isrc']),
			Q("multi_match", query=length, fields=['length'], boost=0.05)])

		s = SoundRecordingDocument.search().query(q)
		qs = s.to_queryset()

		for hit in qs:
			print(hit)
			print(
				"title : {},artitst {}, length:{}".format(hit.title, hit.artist, hit.length)
			)
	