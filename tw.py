from twython import Twython

KEYS = open("KEYS", "r");
APP_KEY = KEYS.readline().strip('\n')
ACCESS_TOKEN = KEYS.readline().strip('\n') # KEYS is a local file
twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

def get_tweet():
    while True:
        statuses = twitter.search(q="",geocode="39.83,-98.58,1500mi")[u'statuses']
        for i in range(len(statuses)):
            try:
                tweet = { "user": statuses[i]["user"]["screen_name"],
                          "created_at": statuses[i]["created_at"],
                          "coordinates": statuses[i]["coordinates"]["coordinates"],
                          "text": statuses[i]["text"]
                        }
                return tweet
            except:
                pass
