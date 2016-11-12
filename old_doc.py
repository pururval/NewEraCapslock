import json
import io
import sys
import re

with open('/home/arun/Desktop/hackathon/testing1234.json','r') as f1:

    for line in f1:
        x = json.loads(line)
        x11 = {}
       
        x11['text_tweet'] = x['text']
        x11['tweet_lang'] = x['lang']
        x11['tweet_loc'] = x['coordinates']
        x11['tweet_date'] = x['created_at']

        x1 = x['text']

        x11['tweet_url'] = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',x1)
        x1 = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',"",x1)

        x11['hashtags'] = re.findall(r"#(\w+)",x1)
        x1 = re.sub(r"#(\w+)","",x1)
       
        x11['mentions'] = re.findall(r"@(\w+)",x1)
        x1 = re.sub(r"@(\w+)","",x1)

        text1 = 'text_'+ x['lang']
        x11[text1] = x1

        if x11['tweet_loc'] != None:
            coordinates = x['tweet_loc']['coordinates'] 
            x11['tweet_loc'] = str(coordinates[1])+', '+str(coordinates[0])

        with open('processed1.json','a') as f2:
            f2.write(json.dumps(x11,f2))
            f2.write('\n')