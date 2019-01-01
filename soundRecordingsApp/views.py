from django.contrib import messages
from django.http import Http404
from django.conf import settings
import logging

from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer

from elasticsearch_dsl import Q

from soundRecordingsApp.serializers import SoundRecordingModelSerializer,SoundRecordingInputModelSerializer,SoundRecordingInputMatchesSerializer

from soundRecordingsApp.models import SoundRecording, SoundRecordingInput, SimilarityScores
from soundRecordingsApp.es_documents import SoundRecordingDocument

ES_INDEX = settings.ES_INDEX



def get_matches(soundRecordingInputs):
	
	for recordingInput in soundRecordingInputs:
		serializedRecording = SoundRecordingInputModelSerializer(recordingInput)
		artist =serializedRecording.data.get('artist') 
		title =serializedRecording.data.get('title')
		isrc =serializedRecording.data.get('isrc')
		length =serializedRecording.data.get('length')

		q = Q('bool',should=[
			Q("multi_match", query=artist, fields=['artist'], fuzziness="AUTO", boost=0.5),
			Q("multi_match", query=title, fields=['title'], fuzziness="AUTO", boost=0.5),
			Q("match",isrc=isrc),
			# The length match should only count if one of the previous fields is positive (havent )
			Q("multi_match", query=length, fields=['length'], boost=0.05)])

		s = SoundRecordingDocument.search().query(q)

		qs = s.to_queryset()


		bulk_list = []
		# The similarity score will be the elastic search score, and since it is given in order i will just store the position, being the lowest number the highest score.
		for score, hit in enumerate(qs):			
			similarityScore = SimilarityScores(soundRecordingInput=recordingInput, soundRecording=hit, score=score )
			bulk_list.append(similarityScore)
		
		SimilarityScores.objects.bulk_create(bulk_list)



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
	
	lines = lines[1:-1]

	bulk_list = []
	# TODO : validate and sanitize CSV file fields.
	for line in lines:
		fields = line.split(",")
		print(len(line))
		if (len(line)==0):
			continue
		data_dict = {}
		try:
			data_dict["artist"] = fields[0].replace('"', '')
			data_dict["title"] = fields[1].replace('"', '')
			data_dict["isrc"] = fields[2].replace('"', '')
			data_dict["length"] = fields[3].replace('"', '')
	
		except IndexError as e:
			# if no more fields are found just continue
			pass
		
		bulk_list.append(Model(**data_dict))
	
	# TODO: add batches in bulk create for allowing the upload of bigger files.
	return Model.objects.bulk_create(bulk_list)
	




class SoundRecordingInputDetail(APIView):
	def get_object(self, pk):
		try:
			return SoundRecordingInput.objects.get(pk=pk)
		except SoundRecordingInput.DoesNotExist:
			raise Http404

	def put(self, request, pk, format=None):
		current = self.get_object(pk)
		matchId = self.request.data.get('matchId', None)

		if(matchId == None):
			match = None
		else:
			match =SoundRecording.objects.get(pk=matchId)
			
		try:
			current.selectedCandidate = match
			current.save()
		except Exception as e:
			return Response(repr(e), status=status.HTTP_400_BAD_REQUEST)
		
		
		return Response("Sound Records Saved", status=status.HTTP_201_CREATED)
		



class SoundRecordingInputList(APIView):

	def get(self, request, format=None):
		unMatchedSoundRecordingInputs = SoundRecordingInput.objects.filter(selectedCandidate=None)
		serializer = SoundRecordingInputMatchesSerializer(unMatchedSoundRecordingInputs, many=True)
		return Response(serializer.data)

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
		allSoundRecordings= SoundRecording.objects.all()
		serializer = SoundRecordingModelSerializer(allSoundRecordings, many=True)
		return Response(serializer.data)


	def post(self, request, format=None):
		try:		
			upload(request, 'db_record')
		except Exception as e:
			logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
			return Response(repr(e), status=status.HTTP_400_BAD_REQUEST)
		# When updating the db all similarity scores will be reindexed, so the similarity scores will be deleted.This is probably not the most efficient/elegant way to do it  :(
		SimilarityScores.objects.all().delete()
		get_matches(SoundRecordingInput.objects.all())

		return Response("Sound Records Saved", status=status.HTTP_201_CREATED)


