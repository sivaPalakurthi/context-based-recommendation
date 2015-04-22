import bottle # Web server
from bottle import run, route, request
import json

from Scrapper import *
from Utilities import *
from TopicModel import *
from Context import *
from Recommendation import *

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
    
    if url is not None:
        utl = Utilities();
        inDB = utl.checkUrlInDb(url);         
        if(inDB == False):
            content = Scrapper().scrap(url);
            topicModel = TopicModel().model(content);
            utl.updateUrl(url,timestamp,user,topicModel);
        else:
            topicModel = utl.getModel(url);
            
        
        ctxt = Context();
        obj = ctxt.updateOrBuild(url,timestamp,user,topicModel);
        #   returns present context details
        
        rcmnd = Recommendation();
        rcmndUrls = rcmnd.recommend(obj);
        
        respObj = {}
        respObj["public"] = rcmndUrls;
        respObj["private"] = ["private1.html","private2.html"];        
                            
        return json.dumps(respObj, indent=4)

if __name__ == '__main__':        
    bottle.debug(True)
    run(host='localhost', port=8000, reloader=True)