import pymongo
import sys
from pymongo import MongoClient

client = MongoClient()

db = client['students']

grades = db['grades']

cur =  grades.find({'type' : 'homework'})
cur.sort([('student_id',pymongo.ASCENDING), ('score', pymongo.ASCENDING)])

# remove the lowest homework score
preStudentId = 0
minScore = 1000
minScoreId = ''
deleteId = []

for entry in cur:

	if entry['student_id'] != preStudentId:
		# we are in a new student
		# process the previous student
		deleteId.append(minScoreId)

		preStudentId = entry['student_id'] 
		minScore = entry['score']
		minScoreId = entry['_id']
	else:
		if entry['score'] < minScore:
			minScore = entry['score']
			minScoreId = entry['_id']

deleteId.append(minScoreId)
for id in deleteId:
	grades.delete_one({'_id' : id})

sanity = 0
for entry in cur:
	print entry
	sanity += 1
	if sanity > 4:
		break
