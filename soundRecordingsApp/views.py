from django.contrib import messages
from django.http import Http404

from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer

from elasticsearch_dsl import Q

import logging
from django.views.decorators.csrf import csrf_exempt

from soundRecordingsApp.serializers import SoundRecordingInputModelSerializer
from soundRecordingsApp.models import SoundRecording, SoundRecordingInput
from soundRecordingsApp.serializers import SoundRecordingInputModelSerializer
from soundRecordingsApp.models import SoundRecording, SoundRecordingInput
from soundRecordingsApp.es_documents import SoundRecordingDocument




def get_matches(soundRecordingInputs):
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

		# for hit in qs:
			
	

def upload(request, type):
	data = {}

	if type=='db_record':
		Model = SoundRecording
	elif type=='input_record':		
		Model = SoundRecordingInput
	else:
		raise TypeError('Only db_record or input_record allowed')

	csv_file = request.FILES["csv_file"]

	if not csv_file.name.endswith('.csv'):
		raise TypeError('File is not CSV Type')
	# TODO: allow the uploading of big files.(by adding threads and bulk_insert by chunks maybe?)	

	# multiple_chunks Returns True if the file is large enough to require multiple chunks to access all of its content give some chunk_size.(default 64kb)
	if csv_file.multiple_chunks():
		messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))

	
	file_data = csv_file.read().decode("utf-8")
	
	lines = file_data.split("\n")
	
	# TODO : validate CSV file fields.
	lines = lines[1:-1]

	bulk_list = []
	for line in lines:						
		fields = line.split(",")
		data_dict = {}
		data_dict["artist"] = fields[0]
		data_dict["title"] = fields[1]
		data_dict["isrc"] = fields[2]
		data_dict["length"] = fields[3]

		bulk_list.append(Model(**data_dict))
	
	# TODO: add batches in bulk create for allowing the upload of bigger files.
	return Model.objects.bulk_create(bulk_list)






class SoundRecordingInputList(APIView):

	def get(self, request, format=None):
		return Response({'response':'ok'})

	# def put(self, request, format=None):
	# 	snippets = SoundRecordingInput.objects.all()
	# 	serializer = SoundRecordingInputModelSerializer(snippets, many=True)

	def post(self, request, format=None):
		try:		
			uploaded_records = upload(request, 'input_record')
		except Exception as e:
			logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
			return Response(repr(e), status=status.HTTP_400_BAD_REQUEST)
		
		get_matches(uploaded_records)

		return Response('ok', status=status.HTTP_201_CREATED)



class SoundRecordingList(APIView):

	def get(self, request, format=None):
		return Response({'response':'ok'})

	# def put(self, request, format=None):
	# 	snippets = SoundRecordingInput.objects.all()
	# 	serializer = SoundRecordingInputModelSerializer(snippets, many=True)

	def post(self, request, format=None):
		try:		
			records = upload(request, 'db_record')
		except Exception as e:
			logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
			return Response(repr(e), status=status.HTTP_400_BAD_REQUEST)

		get_matches(SoundRecordingInput.objects.all())
		return Response({'msg':'ok'}, status=status.HTTP_201_CREATED)
