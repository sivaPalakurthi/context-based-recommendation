# -*- coding: utf-8 -*-

import json

class Context:

    def __init__(self):
        self.thresholdCtxt = 30*60*1000;
        None
            
    def updateOrBuild(self, utl, url,timestamp,user,topicModel):
        # Update or build-new context
        lastCtxt = utl.getLastContext(user);
        #print lastCtxt
        print "some"
        print timestamp
        print lastCtxt
        if( lastCtxt != None and (float(timestamp) - float(lastCtxt['timestamp'])) < self.thresholdCtxt):
            print "111111111111"
            return utl.updateContext(lastCtxt, url, timestamp, topicModel)
        else:
            print "222222222222"
            return utl.buildNewContext(lastCtxt, url, timestamp, user, topicModel)                