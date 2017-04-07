import pymongo
import sys
from pymongo import MongoClient

client = MongoClient()

db = client['school']

grades = db['students']

cur =  grades.find({'scores.type' : 'homework'})
cur.sort([('student_id',pymongo.ASCENDING)])

# remove the lowest homework score
for entry in cur:
	minScore = 1000
	for score in entry['scores']:
		if score['type'] == 'homework':
			if score['score'] < minScore:
				minScore = score['score']
	r = grades.update({'_id' : entry['_id']}, {"$pull": {'scores': {'type' : 'homework', 'score': minScore}}})

sanity = 0
for entry in cur:
	print entry
	sanity += 1
	if sanity > 4:
		break
