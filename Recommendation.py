# -*- coding: utf-8 -*-

import pymongo
from pymongo import MongoClient
import json
from BitVector import *

class Recommendation:

    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.cbr
        self.ctxts_c = self.db.contexts
        self.recommend_c = self.db.recommend
        self.thresholdScore = 0.65;
        self.maxContextSearch = 10000
        
    def score(self, o_context, c_context):
        o_context = BitVector(bitstring = o_context)
        c_context = BitVector(bitstring = c_context)
        return c_context.jaccard_similarity(o_context)
        
    def recommend(self,ctxt):
        # Takes a url as input, returns true if found in db, else returns false
        cList = self.ctxts_c.find().sort('timestamp',-1)
        
        close_ctxt = {}
        similarity = 0;
        ind = 0
        
        for each_ctxt in cList:
            if(each_ctxt['_id'] == ctxt['_id']):
                continue
                
            print "-------------------------"
            print each_ctxt
            print ctxt
            print "-------------------------"
            sc = self.score(each_ctxt['cat'],ctxt['cat'])
            if(sc>similarity):
                similarity = sc;
                close_ctxt = each_ctxt
                if(sc>=self.thresholdScore):
                    break;
            
            # max number of searches
            ind+=1
            if(ind == self.maxContextSearch):
                break;
        if(close_ctxt == {}):
            return None
        urls = close_ctxt['url']
        if(len(urls)>=3):
            return urls[:2]
        else:
            return urls