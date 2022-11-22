import tweepy

#Setup authentication
auth=tweepy.OAuth2BearerHandler("")
api=tweepy.API(auth)

tweets=api.search_tweets("kerala",tweet_mode="extended")

for tweet in tweets:
    print(tweet.full_text)
    print("======================")
