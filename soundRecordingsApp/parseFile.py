
def parseFile(files):
try:
		csv_file = request.FILES["csv_file"]
		if not csv_file.name.endswith('.csv'):
			messages.error(request,'File is not CSV type')
			return ResponseRedirect(reverse("api:upload_csv"))
		#if file is too large, return
		if csv_file.multiple_chunks():
			messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
			return ResponseRedirect(reverse("api:upload_csv"))

		file_data = csv_file.read().decode("utf-8")		
		print(file_data)
		
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
				# print(data_dict)

				soundRecordingForm = SoundRecordingInput(**data_dict)
				# soundRecordingForm.getSimilarityScores()
				# bulk_list.append(soundRecordingForm)
				# SoundRecording.objects.bulk_create(bulk_list)
				if True:
					soundRecordingForm.save()
					print('ok')								
				else:
					logging.getLogger("error_logger").error("form.errors.as_json()")												
			except Exception as e:
				logging.getLogger("error_logger").error(repr(e))					
				pass
		# SoundRecordingInput.objects.bulk_create(bulk_list)

	except Exception as e:
		logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
		messages.error(request,"Unable to upload file. "+repr(e))