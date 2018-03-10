# Dependencies
import tweepy
import json
import time

# Twitter API Keys
consumer_key = "fjsafdjsaklfdjdlsfjdkd"
consumer_secret = "yAOp0FsCNRNEKomJzb0mMLRGo2GWelQUK3O2wgM8tfNCZFTlSQ"
access_token = "97576524-DgEMdCI8GQ5QI9n8KR18NyPtZmgmxW5AWvwpCdqzj"
access_token_secret = "vu95B5DwWAnbZJMoWbh0RmpggElK2wV0Kin9EM9DTkqKN"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
def TweetOut(tweet_number):
    api.update_status(
        "Can't stop. Won't stop. Chatting! This is Tweet #%s!" %
        tweet_number)


# Create a function that calls the TweetOut function every minute
counter = 0

# Infinitely loop
t_end = time.time() + 60 * 10
while(time.time() < t_end):

    # Call the TweetQuotes function and specify the tweet number
    TweetOut(counter)

    # Once tweeted, wait 60 seconds before doing anything else
    time.sleep(60)

    # Add 1 to the counter prior to re-running the loop
    counter = counter + 1