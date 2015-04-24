# -*- coding: utf-8 -*-
#http://www.hasbro.com/en-us/terms
#input = {'privacy':{'p':[{'name':'Our privacy policy explains how we treat your personal data and protect your privacy when you use our Services. By using our Services, you agree that Google can use such data in accordance with our privacy policy.'}
#                        ,{'name':"You will ensure that at all times you use the Services, the Properties have a clearly labeled and easily accessible privacy policy that provides end users with clear and comprehensive information about cookies, device-specific information, location information and other information stored on, accessed on, or collected from end users’ devices in connection with the Services, including, as applicable, information about end users’ options for cookie management.  You will use commercially reasonable efforts to ensure that an end user gives consent to the storing and accessing of cookies, device-specific information, location information or other information on the end user's device in connection with the Services where such consent is required by law."}] },
#        'taxes':{'p':[{'name':'As between you and Google, Google is responsible for all taxes (if any) associated with the transactions between Google and advertisers in connection with Ads displayed on the Properties.  You are responsible for all taxes (if any) associated with the Services, other than taxes based on Google’s net income.  All payments to you from Google in relation to the Services will be treated as inclusive of tax (if applicable) and will not be adjusted.'}] }
#       }    
import requests
import os
import json
from bs4 import BeautifulSoup
import codecs
from aylienapiclient import textapi

class Scrapper:

    def __init__(self):
        None
    
    def rmGarbage(self,strr):
        val=["browser","cookies","signing in", "all rights reserved"] # append bullshit words here to filter more and more
        for each in val:
            if(each.lower() in strr.lower()):
                return False
        return True
        
    def scrap(self,url):
        # returns content of url as a single string
        
        html_doc=requests.get(url)
        html_doc= html_doc.content  # get all content of webpage
        html_doc=''.join([i if ord(i) < 128 else '' for i in html_doc]) # remove utf-8
        soup = BeautifulSoup(html_doc) # reform webpage
        try:
	    title = soup.title.string 
        except:
	    title = url
	para=soup.find_all("p")
        paralist=[]
        para=str(para).replace("[","").replace("]","").replace("u'","")
        para=BeautifulSoup(para)
        
        for each in para.find_all("p"):
            paralist.append(each.get_text())
        
        #Filter some garbage values
        paralistgrb=paralist[:]
        paralist=[]
        content = "";
        for each in paralistgrb:
            if(self.rmGarbage(each)):
                content = content+" " + each                
        return content
            
#url = "http://www.hasbro.com/en-us/terms"
#ob = Scrapper()
#ob.scrap(url)
