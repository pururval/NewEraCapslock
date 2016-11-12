import json
import sys
import tweepy
import time
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

c_key = 'baXihwMIlyRvWX7y1b6n7OZ4G'
c_secret = 'NjsIEoWh0fLzEYmhi50T3dPlGJDfp0nJBz74v2xnGWEVkpBbgA'
access_token = '772223557401243648-zOmAjR7o2zkUr7DxbHgt1jVrN2P9NnW'
access_secret = 'z8VVETm5iC7UL2jlNbSe5AqCGyYjeeDbQwfIwiOsuGW6d'
global count
count = 0
print "hi"
class listener(StreamListener):
    def on_data(self, data):
        try:
            x = json.loads(data)
            if not x["text"].startswith("RT") :
                print data
                global count
                count += 1
                print(count)
                #saveFile = open('test_file.csv','a')
                #saveFile.write(data)
                #saveFile.write('\n')
                #saveFile.close()
                saveFile1 = open('test_file.json','a')
                saveFile1.write(data)
                #saveFile1.write('\n')
                saveFile1.close()
                return True
        except BaseException, e:
            print 'failed ondata,',str(e)
            time.sleep(5)

    def on_error(self, status):
        print status

auth = OAuthHandler(c_key,c_secret)
auth.set_access_token(access_token,access_secret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=['NewEraCap,#NewEra,@NewEraHackathon,@NewEraCap,@NewEra','NewEraHackathon','59FIFTY','#59FIFTY','#ThisIsTheCap'],languages=['en','es','ko'])
