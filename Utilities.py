# -*- coding: utf-8 -*-

import json
import pymongo
from pymongo import MongoClient

class Utilities:

    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.cbr
        self.url_c = self.db.url
        self.ctxts_c = self.db.contexts
        
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
    
    def getLastContext(self,user):
        
        return self.ctxts_c.find_one({"user":user, "latest":True})
    
    def buildNewContext(self, lastCtxt, url, timestamp, user, topicModel):
        
        if(lastCtxt != None):
            lastCtxt['latest'] = None;
            self.ctxts_c.save(lastCtxt)     
        self.ctxts_c.insert({"url":[url],"timestamp":timestamp,"user":user,"cat":topicModel,"latest":True})
       
    def updateContext(self, lastCtxt, url, timestamp, topicModel):
       
       lastCtxt['url'].append(url)
       print topicModel
       lastCtxt['cat'] = lastCtxt['cat'] + topicModel
       self.ctxts_c.save(lastCtxt)
    
    
    
       
       
       


