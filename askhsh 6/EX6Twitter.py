import tweepy

consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)

userID = (input("Δώσε όνομα χρήστη: "))

tweets = api.user_timeline(screen_name=userID, count=10, include_rts = False, tweet_mode = 'extended')
text = ""
for info in tweets[:10]:
     text = text + (info.full_text)
text = list(text.split(" "))
text = sorted(text, key=len)
print(text[:5])
print(text[:-6:-1])
