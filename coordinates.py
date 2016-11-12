import json
import io
import sys
import re
import numpy as np
import geojson
from geojson import Point

with open('/home/arun/Desktop/hackathon/test_file.json','r') as f1:

    location = []
    for line in f1:
        x = json.loads(line)
        x11 = {}
       
        #x11['text_tweet'] = x['text']
        #x11['tweet_lang'] = x['lang']
        #x11['tweet_loc'] = x['coordinates']
        #x11['tweet_date'] = x['created_at']

        #x1 = x['text']

        #x11['tweet_url'] = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',x1)
        #x1 = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',"",x1)

        #x11['hashtags'] = re.findall(r"#(\w+)",x1)
        #x1 = re.sub(r"#(\w+)","",x1)
       
        #x11['mentions'] = re.findall(r"@(\w+)",x1)
        #x1 = re.sub(r"@(\w+)","",x1)

        #text1 = 'text_'+ x['lang']
        #x11[text1] = x1

        if x['coordinates'] != None:
            #print "hi"
            coordinates = x['coordinates']['coordinates']
            print coordinates
            location.append(coordinates) 
            #x11['location'] = str(coordinates[1])+', '+str(coordinates[0])

with open('final45.json','a') as f2:
    f2.write(json.dumps(location,f2))
    #f2.write('\n')
#Point((location))
#print Point
