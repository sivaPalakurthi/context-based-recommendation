import bottle # Web server
from bottle import run, route, request
import json
import datetime
from Scrapper import *
from Utilities import *
from TopicModel import *
from Context import *
from Recommendation import *

utl = Utilities();
sc = Scrapper();
tm = TopicModel();
ctxt = Context();
rcmnd = Recommendation();
        
@route('/')
def index():
    """ Display welcome & instruction messages """
    return "<p>Welcome to my extra simple bottle.py powered server !</p> \
    	   <p>There are two ways to invoke the web service :\
	   <ul><li>http://localhost:8080/up?s=type_your_string_here</li>\
	   <li>http://localhost:8080/up?URL=http://url_to_file.txt</li></ul>"

@route('/recommend')
def uppercase():  
    
    url   = request.GET.get('url'  , default=None)
    timestamp   = request.GET.get('timestamp'  , default=None)    
    user   = request.GET.get('user'  , default=None)    
    title   = request.GET.get('title'  , default=None)    
    
    if(timestamp == None):
        timestamp = int(datetime.datetime.now().strftime("%s")) * 1000
    
    print url
    print timestamp
    print user
    if url is not None:
        
        topicModel = utl.checkUrlInDb(url); 
                
        if(topicModel == False):
            content = sc.scrap(url);
            topicModel = tm.model([content]);
            utl.updateUrl(url,timestamp,user,topicModel);
        
        utl.updateUserModel(user, topicModel);
        obj = ctxt.updateOrBuild(utl, url, timestamp, user, topicModel);
        #   returns present context details
        print "Contexttttt"
        print obj
        rcmndUrls = rcmnd.recommend(obj);
        
        respObj = {}
        respObj["public"] = rcmndUrls;
        respObj["private"] = ["private1000.html","private2.html"];        
                            
        print "SSSSSSSSSSSSSSSSSSS"
        print "Recommended Articles"
        print rcmndUrls
        print "EEEEEEEEEEEEEEEEEEE"
        
        return json.dumps(respObj, indent=4)

if __name__ == '__main__':        
    bottle.debug(True)
    run(host='localhost', port=8000, reloader=True)
