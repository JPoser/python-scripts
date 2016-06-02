import os, exifread, json
from sys import argv

script, directory = argv

photos = []
geo_data = {}

# get list of photos
for root, dirs, files in os.walk(directory):
	for f in files:
		if f.endswith(".JPG"):
			photos.append(os.path.join(root, f))

# create dictionary geo_data of gps co-ordinates
for photo in photos:
	open_photo = open(photo, 'rb')
	tags = exifread.process_file(open_photo)
	geo = {i:tags[i] for i in tags.keys() if i.startswith('GPS')}
	print geo
	open_photo.close()