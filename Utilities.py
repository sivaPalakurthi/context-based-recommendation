# -*- coding: utf-8 -*-
import json
import pymongo
from pymongo import MongoClient
from BitVector import *

class Utilities:

    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.cbr
        self.url_c = self.db.url
        self.ctxts_c = self.db.contexts
        self.users_c = self.db.users
        self.categories={'hardware': 4, 'christian': 15, 'motorcycles': 8, 'med': 13, 'crypt': 11, 'space': 14, 'misc': 19, 'atheism': 0, 'autos': 7, 'baseball': 9, 'hockey': 10, 'mideast': 17, 'graphics': 1, 'x': 5, 'electronics': 12, 'forsale': 6, 'guns': 16};
        
    def tmToBitVector(self,tm):
        
        vec = BitVector(size=len(self.categories)+3)
        for each in tm:
            vec[self.categories[each]]=1
        return vec
          
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
        print "In buildNew Context"
        if(lastCtxt != None):
            lastCtxt['latest'] = None;
            self.ctxts_c.save(lastCtxt)     
        self.ctxts_c.insert({"url":[url],"timestamp":timestamp,"user":user,"cat":str(self.tmToBitVector(topicModel)),"latest":True})
        return self.ctxts_c.find_one({"url":[url],"timestamp":timestamp})
        
    def updateContext(self, lastCtxt, url, timestamp, topicModel):
       print "In Update Context"
       found = False;
       print "333333333"
       for each in lastCtxt['url']:
           if(each == url):
               found = True
       print "555555555"
       if(found == False):
           lastCtxt['url'].append(url)
           print "66666666"
           tm = BitVector(bitstring = lastCtxt['cat'])
           print "Topic Model"
           print topicModel
           for each in topicModel:
               tm[self.categories[each]] = 1
               lastCtxt['cat'] = str(tm)
        
           self.ctxts_c.save(lastCtxt)
           print lastCtxt
           print "Exiting Update Context"
       return lastCtxt
    
    def updateUserModel(self, user, topicModel):
        userModel = self.users_c.find_one({"user":user})
        if(userModel == None):
            self.users_c.insert({"user":user})
            userModel = self.users_c.find_one({"user":user})
        for each in topicModel:
            if(each in userModel):
                userModel[each]+=1
            else:
                userModel[each]=1
        self.users_c.save(userModel)