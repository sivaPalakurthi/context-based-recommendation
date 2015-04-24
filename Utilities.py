# -*- coding: utf-8 -*-

import json
import pymongo
from pymongo import MongoClient

class Utilities:

    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.cbr
        self.url_c = self.db.url
        
    def checkUrlInDb(self,url):
        # Takes a url as input, returns 'categories' if found in db, else returns false
        rec = self.url_c.find_one({"url": url})
        if(rec == None):
            return False
        return rec['cat']
        
    def updateUrl(self,url,timestamp,user,topicModel):
        # Takes a url as input, add to Url's collection
        self.url_c.insert({"url":url,"timestamp":timestamp,"user":user,"cat":topicModel})
        return True            
    
    #def getModel(self,url):
    #    # Takes a url and return categories
    #    return ["cat1","cat2"]