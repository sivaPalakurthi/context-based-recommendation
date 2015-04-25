# -*- coding: utf-8 -*-

import json

class Context:

    def __init__(self):
        self.thresholdCtxt = 30*60;
        None
            
    def updateOrBuild(self, utl, url,timestamp,user,topicModel):
        # Update or build-new context
        lastCtxt = utl.getLastContext(user);
        print lastCtxt
        if( lastCtxt != None and (float(timestamp) - float(lastCtxt['timestamp'])) < self.thresholdCtxt):
            utl.updateContext(lastCtxt, url, timestamp, topicModel)
        else:
            utl.buildNewContext(lastCtxt, url, timestamp, user, topicModel)
        
        return True