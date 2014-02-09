from twython import Twython

APP_KEY = "OZ6EFUr3RGRzjmM6SOWPA"
APP_SECRET = "9SudGPes8ixj0HnEz4emxWNuIp5TTh8LGo3bxKUU"

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()
print ACCESS_TOKEN
