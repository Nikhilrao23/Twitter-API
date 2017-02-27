from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

cKey = ''
cSecret = ''
aToken = ''
aSecret = ''

class ListenerStream(StreamListener):

    def on_data(self, raw_data):
        try:
            print (raw_data)
            saveFile = open("Filename.csv", "a")
            saveFile.write(raw_data)
            saveFile.write("\n")
            saveFile.close()
            return True

        except Exception as e:
            print ("Error on Data")
            time.sleep(5)

    def on_error(self, status_code):
        print (status_code)

auth = OAuthHandler(cKey, cSecret)
auth.set_access_token(aToken, aSecret)
twitterStream = Stream(auth, ListenerStream())
twitterStream.filter(track = ["India"])
