#!/usr/bin/env python

from pymongo import MongoClient
import json
from pprint import pprint
import sys
import os

DB_NAME = 'recsys'

client = MongoClient('localhost', 27017)
db = client[DB_NAME]

HOME_USER = os.path.expanduser('~')
path = HOME_USER +  "/data/recsys/"

playlists_collection = db.playlists
playlists_collection.delete_many({})

for filename in os.listdir(path):
	file_path = os.path.join(path, filename)

	with open(file_path) as f:
		data = json.load(f)

		playlists_jsons = data['playlists']

		for playlist in playlists_jsons:
			playlists_collection.insert_one(playlist)
