from soundRecordingsApp.models import SoundRecording, SoundRecordingInput
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django.contrib import messages

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer

import logging

from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
def upload_csv(request):
	data = {}

	if "GET" == request.method:
		return Response("Hello, world. You're at the matchers index.")
	# if not GET, then proceed
	try:
		csv_file = request.FILES["csv_file"]
		# if not csv_file.name.endswith('.csv'):
		# 	messages.error(request,'File is not CSV type')
		# 	return ResponseRedirect(reverse("musicApi:upload_csv"))
		# #if file is too large, return
		# if csv_file.multiple_chunks():
		# 	messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
		# 	return ResponseRedirect(reverse("musicApi:upload_csv"))

		file_data = csv_file.read().decode("utf-8")		
		
		lines = file_data.split("\n")
		lines = lines[1:-1]

		#loop over the lines and save them in db. If error , store as string and then display

		bulk_list = []
		for line in lines:						
			fields = line.split(",")
			data_dict = {}
			data_dict["artist"] = fields[0]
			data_dict["title"] = fields[1]
			data_dict["isrc"] = fields[2]
			data_dict["length"] = fields[3]
			try:
				serializer = SoundRecording(**data_dict)
				bulk_list.append(serializer)
															
			except Exception as e:
				logging.getLogger("error_logger").error(repr(e))					
				pass

		SoundRecording.objects.bulk_create(bulk_list)

	except Exception as e:
		logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
		messages.error(request,"Unable to upload file. "+repr(e))

	Response.accepted_renderer = JSONRenderer()
	Response.accepted_media_type = "application/json"
	Response.renderer_context = {}

	return Response({'response':'ok'})
