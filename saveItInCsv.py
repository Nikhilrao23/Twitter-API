from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

cKey = 'jrE3NLy3FMdJBg5XBBy6FewKG'
cSecret = 'zw0z4vMePFepwV4C1c6D4W7Umj8sa7YahWfxShgqdrSdypl3X8'
aToken = '251123508-Z3SpWsW0OIsxrBvOezMjE1VYXGUYJS2STLMLoJZo'
aSecret = 'sZ6auKLckq2EtjV2kzTGHEwnPG2hholJXaGBEN2oT9caT'

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
