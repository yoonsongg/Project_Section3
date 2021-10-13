from pymongo import MongoClient
import json
import os
import csv
import glob
from pathlib import Path
from pprint import pprint

#mongoDB 접속
HOST = 'cluster0.bvo67.mongodb.net'
USER = 'whaleuser'
PASSWORD = 'song0909'
DATABASE_NAME = 'Project3'
# COLLECTION_NAME = 'grade7_correct'
MONGO_URI = f"mongodb+srv://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}?retryWrites=true&w=majority"


client = MongoClient(MONGO_URI)
database = client[DATABASE_NAME]
# collection = database[COLLECTION_NAME + '_train']
# collection_valid = database[COLLECTION_NAME + '_valid']

#collection.insert_many(octokit)
#collection.insert_one({'Hello':1})

#json data 읽어서 collection에 저장  
BASE_DIR = os.getcwd() + '/' + 'data' 
DIR_Training = BASE_DIR + '/' + 'Training' + '/' + 'achievement_dataset_train/7th'
DIR_Validation = BASE_DIR + '/' + 'Validation' + '/' + 'achievement_dataset_valid/7th'
# file =  '/' + '실력평가001' + '/1_문항정오답표' + '/*'

class toMongoDB():
    def __init__(self):
        self.correct = []
        self.filename_path_list =[]
        self.file_list = []
        self.itemIRT = []
        self.learnerIRT = []
        self.file_list_item = []
        self.file_list_learner = []
      
    def search_file(self, dirname):
        path_list = os.listdir(dirname)
        for filename in path_list:
            filename_path = os.path.join(dirname, filename)
            self.filename_path_list.append(filename_path)
    
        for item_correct in self.filename_path_list:
            file_path = os.path.join(item_correct, '1_문항정오답표')
            self.file_list.extend(glob.glob(file_path + '/*'))
  
        for f in self.file_list:
            with open(f, 'r') as f:
                self.correct.append(json.load(f))

        for item_correct in self.filename_path_list:
            file_path = os.path.join(item_correct, '2_문항IRT')
            self.file_list_item.extend(glob.glob(file_path + '/*'))
  
        for f in self.file_list_item:
            with open(f, 'r') as f:
                self.itemIRT.append(json.load(f))
        
        for learner in self.filename_path_list:
            file_path = os.path.join(learner, '3_응시자IRT')
            self.file_list_learner.extend(glob.glob(file_path + '/*'))
  
        for f in self.file_list_learner:
            with open(f, 'r') as f:
                self.learnerIRT.append(json.load(f))
    
        return self.correct, self.itemIRT, self.learnerIRT


a = toMongoDB()
a.search_file(DIR_Training)
database['grade7_correct_train'].insert_many(a.correct)
database['grade7_itemIRT_train'].insert_many(a.itemIRT)
database['grade7_learnerIRT_train'].insert_many(a.learnerIRT)

b = toMongoDB()
b.search_file(DIR_Validation)
database['grade7_correct_valid'].insert_many(b.correct)
database['grade7_itemIRT_valid'].insert_many(b.itemIRT)
database['grade7_learnerIRT_valid'].insert_many(b.learnerIRT)

