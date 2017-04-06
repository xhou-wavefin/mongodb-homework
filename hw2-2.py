import pymongo

from pymongo import MongoClient

client = MongoClient()

db = client['students']

grades = db['grades']

print grades.find_one()