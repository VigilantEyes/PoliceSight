import tweepy
client=tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAKlYiAEAAAAAtig4A0Zi16hZ8BNzw17hbBef%2Fs8%3DyCqSNH5GfLa5Kxh6oQiQPxx7gb7Lv2gcrUKIsyjLsT0UyjJGDK')
query_stmt='#keralapolice lang:en'
tweets=client.search_recent_tweets(query=query_stmt,tweet_fields=['context_annotations','created_at'],max_results=100)
for tweet in tweets.data:
    print(tweet.text)
    print(tweet.created_at)
    print("=====================================")
    #print(tweet.context_annotations)