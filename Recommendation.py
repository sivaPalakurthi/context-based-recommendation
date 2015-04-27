# -*- coding: utf-8 -*-

import pymongo
from pymongo import MongoClient
import json

class Recommendation:

    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.cbr
        self.ctxts_c = self.db.contexts
        self.recommend_c = self.db.recommend
        
    def recommend(self,url):
        # Takes a url as input, returns true if found in db, else returns false
        return ["url1.html","url2.html"]
    
    def batchProcess(self):
        
        cList = self.ctxts_c.find()        
        
        
        
        
        